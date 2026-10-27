"""
Initialisation de la base MySQL 'stock_it' (XAMPP) via mysql-connector-python.

Etape 1 : connexion sans base -> CREATE DATABASE IF NOT EXISTS stock_it
Etape 2 : reconnexion avec database="stock_it" -> CREATE TABLE ...
"""

import os
import sys

try:
    import mysql.connector
    from mysql.connector import errorcode
except ImportError:
    print("[ERREUR] Le module 'mysql-connector-python' n'est pas installe.")
    print("         Installez-le avec : pip install mysql-connector-python")
    sys.exit(1)

DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = ""
DB_NAME = "stock_it"

SQL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema.sql")


def split_sql_statements(sql_text: str):
    """Découpe un script SQL en instructions individuelles (fin sur ';')."""
    statements = []
    current = []
    for raw_line in sql_text.splitlines():
        line = raw_line.split("--", 1)[0].strip()
        if not line:
            continue
        current.append(line)
        if line.endswith(";"):
            stmt = " ".join(current).rstrip(";").strip()
            if stmt:
                statements.append(stmt)
            current = []
    if current:
        stmt = " ".join(current).strip()
        if stmt:
            statements.append(stmt)
    return statements


def connect(with_db: bool):
    kwargs = dict(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS,
        charset="utf8mb4", use_unicode=True, autocommit=True,
    )
    if with_db:
        kwargs["database"] = DB_NAME
    return mysql.connector.connect(**kwargs)


def main():
    if not os.path.isfile(SQL_FILE):
        print(f"[ERREUR] Fichier SQL introuvable : {SQL_FILE}")
        sys.exit(1)

    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql_text = f.read()

    statements = split_sql_statements(sql_text)

    create_db_stmt = None
    other_stmts = []
    for stmt in statements:
        low = stmt.lower().lstrip()
        if low.startswith("create database"):
            create_db_stmt = stmt
        elif low.startswith("use "):
            continue
        else:
            other_stmts.append(stmt)

    print(f"[INFO] Base cible : {DB_NAME}")
    print(f"[INFO] Connexion a {DB_USER}@{DB_HOST}:{DB_PORT} ...")
    try:
        conn = connect(with_db=False)
    except mysql.connector.Error as e:
        print(f"[ERREUR] Connexion MySQL impossible : {e}")
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("[ASTUCE] Verifiez user/password (root / vide sur XAMPP).")
        elif e.errno == 2003:
            print("[ASTUCE] MySQL n'est pas demarre : lancez-le depuis XAMPP.")
        sys.exit(1)

    try:
        cur = conn.cursor()
        if create_db_stmt:
            print(f"  OK  [1] : {create_db_stmt[:70]}...")
            cur.execute(create_db_stmt)
        cur.close()
    finally:
        conn.close()

    print(f"[INFO] {len(other_stmts)} instruction(s) a executer dans '{DB_NAME}'.")
    try:
        conn = connect(with_db=True)
    except mysql.connector.Error as e:
        print(f"[ERREUR] Connexion a la base '{DB_NAME}' impossible : {e}")
        sys.exit(1)

    try:
        cur = conn.cursor()
        for i, stmt in enumerate(other_stmts, 1):
            try:
                cur.execute(stmt)
                try:
                    cur.fetchall()
                except mysql.connector.InterfaceError:
                    pass
                print(f"  OK  [{i}/{len(other_stmts)}] : {stmt[:70]}...")
            except mysql.connector.Error as e:
                print(f"  ERR [{i}/{len(other_stmts)}] : {e}")
                print(f"     Requete : {stmt[:200]}")
                raise
        cur.close()
    finally:
        conn.close()

    print(f"\n[SUCCES] Base '{DB_NAME}' initialisee avec succes.")


if __name__ == "__main__":
    main()