#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peuplement de 'stock_it' (stdlib uniquement).

Nouveau schema :
    Produit       (NumProduit, Design, Stock)
    BondeEntree   (NumBon, NumProduit, QteEntree, DateEntree)
    BondeSortie   (NumBon, NumProduit, QteSortie, DateSortie)

Coherence :
    Stock = SUM(QteEntree) - SUM(QteSortie)
    - On insere d'abord les entrees (creent le stock).
    - On insere ensuite les sorties, jamais plus que dispo.
    - On recalcule Produit.Stock en SQL a la fin.
"""

import sys
import random
import string
from datetime import date, timedelta

try:
    import mysql.connector
    from mysql.connector import errorcode
except ImportError:
    print("[ERREUR] mysql-connector-python manquant : pip install mysql-connector-python")
    sys.exit(1)

# --- Parametres ---
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = ""
DB_NAME = "stock_it"

NB_PRODUITS     = 25
MAX_BONS_ENTREE = 3
MAX_BONS_SORTIE = 3
SEED            = 42

random.seed(SEED)

# --- Vocabulaire ---
MARQUES  = ["Logitech", "HP", "Dell", "Samsung", "Asus", "Lenovo",
            "Canon", "Epson", "TP-Link", "Kingston", "SanDisk", "Acer"]
OBJETS   = ["Clavier", "Souris", "Ecran", "Cable HDMI", "Disque SSD",
            "Cle USB", "Casque", "Webcam", "Imprimante laser", "Switch",
            "Routeur", "Hub USB", "Chargeur", "Batterie", "Adaptateur",
            "Tapis souris", "Support ecran", "Enceinte", "Microphone", "Scanner"]
COULEURS = ["Noir", "Blanc", "Gris", "Bleu", "Rouge", "Vert",
            "Argent", "Or", "Transparent", "Violet", "Orange"]
SUFFIXES = ["Pro", "Max", "Lite", "Plus", "V2", "V3", "Series X",
            "Edition", "Standard", "Compact", "XL"]


# ---------------------------------------------------------------
# Generateurs
# ---------------------------------------------------------------
def gen_design() -> str:
    return " ".join([
        random.choice(MARQUES),
        random.choice(OBJETS),
        random.choice(COULEURS),
        random.choice(SUFFIXES),
    ])


def gen_num_produit(index: int) -> str:
    return f"PRD-{index:04d}"


def _random_code(n: int = 4) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))


def gen_num_bon(prefix: str, used: set) -> str:
    while True:
        d = date.today() - timedelta(days=random.randint(0, 365))
        num = f"{prefix}-{d.strftime('%Y%m%d')}-{_random_code(4)}"
        if num not in used:
            used.add(num)
            return num


def gen_date_in_past(days_max: int = 365) -> date:
    return date.today() - timedelta(days=random.randint(0, days_max))


# ---------------------------------------------------------------
# Connexion
# ---------------------------------------------------------------
def connect():
    try:
        return mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS,
            database=DB_NAME, charset="utf8mb4", use_unicode=True,
            autocommit=False,
        )
    except mysql.connector.Error as e:
        print(f"[ERREUR] Connexion a '{DB_NAME}' impossible : {e}")
        if e.errno == errorcode.ER_BAD_DB_ERROR:
            print("[ASTUCE] Lancez d'abord run.bat (init.py).")
        elif e.errno == 2003:
            print("[ASTUCE] MySQL n'est pas demarre (XAMPP).")
        sys.exit(1)


# ---------------------------------------------------------------
# Peuplement
# ---------------------------------------------------------------
def main():
    print(f"[INFO] Connexion a {DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME} ...")
    conn = connect()
    cur = conn.cursor()

    # 1) Nettoyage
    print("[INFO] Nettoyage des tables existantes ...")
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("TRUNCATE TABLE BondeSortie")
    cur.execute("TRUNCATE TABLE BondeEntree")
    cur.execute("TRUNCATE TABLE Produit")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")

    produits = []
    dispo = {}                       # NumProduit -> stock disponible courant
    bons_entree_used = set()
    bons_sortie_used = set()

    # 2) Produits (Stock = 0 initialement, recalcule a la fin)
    print(f"[INFO] Generation de {NB_PRODUITS} produits ...")
    for i in range(1, NB_PRODUITS + 1):
        num = gen_num_produit(i)
        design = gen_design()
        produits.append(num)
        dispo[num] = 0
        cur.execute(
            "INSERT INTO Produit (NumProduit, Design, Stock) VALUES (%s, %s, 0)",
            (num, design),
        )

    # 3) Bons d'entree
    print("[INFO] Generation des bons d'entree ...")
    for num_produit in produits:
        for _ in range(random.randint(1, MAX_BONS_ENTREE)):
            qte = random.randint(1, 50)
            d = gen_date_in_past(365)
            num_bon = gen_num_bon("BE", bons_entree_used)
            cur.execute(
                "INSERT INTO BondeEntree (NumBon, NumProduit, QteEntree, DateEntree) "
                "VALUES (%s, %s, %s, %s)",
                (num_bon, num_produit, qte, d),
            )
            dispo[num_produit] += qte

    # 4) Bons de sortie (jamais > dispo)
    print("[INFO] Generation des bons de sortie ...")
    for num_produit in produits:
        for _ in range(random.randint(0, MAX_BONS_SORTIE)):
            if dispo[num_produit] <= 0:
                break
            qte = random.randint(1, min(dispo[num_produit], 40))
            d = gen_date_in_past(365)
            num_bon = gen_num_bon("BS", bons_sortie_used)
            cur.execute(
                "INSERT INTO BondeSortie (NumBon, NumProduit, QteSortie, DateSortie) "
                "VALUES (%s, %s, %s, %s)",
                (num_bon, num_produit, qte, d),
            )
            dispo[num_produit] -= qte

    # 5) Recalcul du Stock reel (pas de StockInitial dans ce schema)
    print("[INFO] Recalcul du champ Stock ...")
    cur.execute("""
        UPDATE Produit p
        SET p.Stock =
              COALESCE((SELECT SUM(be.QteEntree) FROM BondeEntree be
                        WHERE be.NumProduit = p.NumProduit), 0)
            - COALESCE((SELECT SUM(bs.QteSortie) FROM BondeSortie bs
                        WHERE bs.NumProduit = p.NumProduit), 0)
    """)

    conn.commit()

    # 6) Resume
    cur.execute("SELECT COUNT(*), COALESCE(SUM(Stock),0) FROM Produit")
    nb_p, total_stock = cur.fetchone()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(QteEntree),0) FROM BondeEntree")
    nb_be, total_be = cur.fetchone()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(QteSortie),0) FROM BondeSortie")
    nb_bs, total_bs = cur.fetchone()

    print("\n" + "=" * 50)
    print("  RESUME DU PEUPLEMENT")
    print("=" * 50)
    print(f"  Produits       : {nb_p:>4}   (stock cumule : {total_stock})")
    print(f"  Bons d'entree  : {nb_be:>4}   (quantite    : {total_be})")
    print(f"  Bons de sortie : {nb_bs:>4}   (quantite    : {total_bs})")
    print("=" * 50)
    print(f"[SUCCES] Base '{DB_NAME}' peuplee.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()