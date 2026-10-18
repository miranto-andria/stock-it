import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "stock_it",
}


def connect():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        raise Error(f"Erreur de connexion : {e}") from e


def execute(query, params=None, fetch=False):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        conn.rollback()
        raise Error(f"Erreur SQL : {e}") from e
    finally:
        cursor.close()
        conn.close()
def execute_one(query, params=None):
    lignes = execute(query, params, fetch=True)
    if not lignes:
        return None
    return lignes[0]

def execute_many(requetes):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    try:
        for query, params in requetes:
            cursor.execute(query, params or ())
        conn.commit()
    except Error as e:
        conn.rollback()
        raise Error(f"Erreur SQL : {e}") from e
    finally:
        cursor.close()
        conn.close()

def get_entry_pass():
    entry_pass = execute("SELECT * FROM bondeentree" , fetch=True)
    return entry_pass

def product_lists():
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit ORDER BY NumProduit",
        fetch=True,
    )

def search_product(texte):
    texte = (texte or "").strip()
    if not texte:
        return product_lists()
    modele = "%" + texte + "%"
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit "
        "WHERE NumProduit LIKE %s OR Design LIKE %s ORDER BY NumProduit",
        (modele, modele),
        fetch=True,
    )

def count(query, params=None):
    ligne = execute_one(query, params)
    if ligne is None or ligne["total"] is None:
        return 0
    return ligne["total"]


def get_total_products():
    return count("SELECT COUNT(*) AS total FROM Produit")


def get_nb_bons_entree():
    return count("SELECT COUNT(*) AS total FROM BondeEntree")


def get_nb_bons_sortie():
    return count("SELECT COUNT(*) AS total FROM BondeSortie")


def get_total_stock():
    return count("SELECT COALESCE(SUM(Stock), 0) AS total FROM Produit")

def stock_repartition():
    return [
        (
            "Rupture(0)",
            count("SELECT COUNT(*) AS total FROM Produit WHERE Stock <= 0"),
        ),
        (
            "Faible(1-5)",
            count("SELECT COUNT(*) AS total FROM Produit WHERE Stock BETWEEN 1 AND 5"),
        ),
        (
            "Moyen(6-10)",
            count("SELECT COUNT(*) AS total FROM Produit WHERE Stock BETWEEN 6 AND 10"),
        ),
        (
            "Élevé(> 10)",
            count("SELECT COUNT(*) AS total FROM Produit WHERE Stock > 10"),
        ),
    ]