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

DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = ""
DB_NAME = "stock_it"

PRODUCT_COUNT    = 25
MAX_ENTRY_VOUCHERS = 3
MAX_EXIT_VOUCHERS  = 3
SEED              = 42

random.seed(SEED)

BRANDS = ["Logitech", "HP", "Dell", "Samsung", "Asus", "Lenovo",
            "Canon", "Epson", "TP-Link", "Kingston", "SanDisk", "Acer"]
ITEMS  = ["Clavier", "Souris", "Ecran", "Cable HDMI", "Disque SSD",
            "Cle USB", "Casque", "Webcam", "Imprimante laser", "Switch",
            "Routeur", "Hub USB", "Chargeur", "Batterie", "Adaptateur",
            "Tapis souris", "Support ecran", "Enceinte", "Microphone", "Scanner"]
COLORS = ["Noir", "Blanc", "Gris", "Bleu", "Rouge", "Vert",
            "Argent", "Or", "Transparent", "Violet", "Orange"]
SUFFIXES = ["Pro", "Max", "Lite", "Plus", "V2", "V3", "Series X",
            "Edition", "Standard", "Compact", "XL"]


def gen_design() -> str:
    return " ".join([
        random.choice(BRANDS),
        random.choice(ITEMS),
        random.choice(COLORS),
        random.choice(SUFFIXES),
    ])


def gen_product_number(index: int) -> str:
    return f"PRD-{index:04d}"


def _random_code(n: int = 4) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))


def gen_voucher_number(prefix: str, used: set) -> str:
    while True:
        d = date.today() - timedelta(days=random.randint(0, 365))
        num = f"{prefix}-{d.strftime('%Y%m%d')}-{_random_code(4)}"
        if num not in used:
            used.add(num)
            return num


def gen_date_in_past(days_max: int = 365) -> date:
    return date.today() - timedelta(days=random.randint(0, days_max))


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


def main():
    print(f"[INFO] Connexion a {DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME} ...")
    conn = connect()
    cur = conn.cursor()

    print("[INFO] Nettoyage des tables existantes ...")
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("TRUNCATE TABLE BondeSortie")
    cur.execute("TRUNCATE TABLE BondeEntree")
    cur.execute("TRUNCATE TABLE Produit")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")

    products = []
    available = {}
    used_entry_vouchers = set()
    used_exit_vouchers = set()

    print(f"[INFO] Generation de {PRODUCT_COUNT} produits ...")
    for i in range(1, PRODUCT_COUNT + 1):
        num = gen_product_number(i)
        design = gen_design()
        products.append(num)
        available[num] = 0
        cur.execute(
            "INSERT INTO Produit (NumProduit, Design, Stock) VALUES (%s, %s, 0)",
            (num, design),
        )

    print("[INFO] Generation des bons d'entree ...")
    for num_product in products:
        for _ in range(random.randint(1, MAX_ENTRY_VOUCHERS)):
            qty = random.randint(1, 50)
            d = gen_date_in_past(365)
            num_voucher = gen_voucher_number("BE", used_entry_vouchers)
            cur.execute(
                "INSERT INTO BondeEntree (NumBon, NumProduit, QteEntree, DateEntree) "
                "VALUES (%s, %s, %s, %s)",
                (num_voucher, num_product, qty, d),
            )
            available[num_product] += qty

    print("[INFO] Generation des bons de sortie ...")
    for num_product in products:
        for _ in range(random.randint(0, MAX_EXIT_VOUCHERS)):
            if available[num_product] <= 0:
                break
            qty = random.randint(1, min(available[num_product], 40))
            d = gen_date_in_past(365)
            num_voucher = gen_voucher_number("BS", used_exit_vouchers)
            cur.execute(
                "INSERT INTO BondeSortie (NumBon, NumProduit, QteSortie, DateSortie) "
                "VALUES (%s, %s, %s, %s)",
                (num_voucher, num_product, qty, d),
            )
            available[num_product] -= qty

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

    cur.execute("SELECT COUNT(*), COALESCE(SUM(Stock),0) FROM Produit")
    product_count, total_stock = cur.fetchone()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(QteEntree),0) FROM BondeEntree")
    entry_count, total_entry = cur.fetchone()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(QteSortie),0) FROM BondeSortie")
    exit_count, total_exit = cur.fetchone()

    print("\n" + "=" * 50)
    print("  RESUME DU PEUPLEMENT")
    print("=" * 50)
    print(f"  Produits       : {product_count:>4}   (stock cumule : {total_stock})")
    print(f"  Bons d'entree  : {entry_count:>4}   (quantite    : {total_entry})")
    print(f"  Bons de sortie : {exit_count:>4}   (quantite    : {total_exit})")
    print("=" * 50)
    print(f"[SUCCES] Base '{DB_NAME}' peuplee.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()