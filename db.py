from datetime import date

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "stock_it",
}
TABLE_PRODUCT = "Produit"
TABLE_ENTRY = "BondeEntree"
TABLE_EXIT = "BondeSortie"


def connect():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        raise Error(f"Erreur de connexion : {e}") from e


def execute(query, params=None, fetch=False):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        connection.rollback()
        raise Error(f"Erreur SQL : {e}") from e
    finally:
        cursor.close()
        connection.close()


def execute_one(query, params=None):
    rows = execute(query, params, fetch=True)
    if not rows:
        return None
    return rows[0]


def execute_many(queries):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    try:
        for query, params in queries:
            cursor.execute(query, params or ())
        connection.commit()
    except Error as e:
        connection.rollback()
        raise Error(f"Erreur SQL : {e}") from e
    finally:
        cursor.close()
        connection.close()


def get_entry_pass():
    return execute(
        "SELECT b.NumBon, b.NumProduit, b.QteEntree, b.DateEntree, p.Design "
        "FROM BondeEntree b JOIN Produit p ON b.NumProduit = p.NumProduit "
        "ORDER BY b.NumBon",
        fetch=True,
    )


def get_exit_pass():
    return execute(
        "SELECT b.NumBon, b.NumProduit, b.QteSortie, b.DateSortie, p.Design "
        "FROM BondeSortie b JOIN Produit p ON b.NumProduit = p.NumProduit "
        "ORDER BY b.NumBon",
        fetch=True,
    )


def product_lists():
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit ORDER BY NumProduit",
        fetch=True,
    )


def search_product(text):
    text = (text or "").strip()
    if not text:
        return product_lists()
    pattern = "%" + text + "%"
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit "
        "WHERE NumProduit LIKE %s OR Design LIKE %s ORDER BY NumProduit",
        (pattern, pattern),
        fetch=True,
    )


def count(query, params=None):
    row = execute_one(query, params)
    if row is None or row["total"] is None:
        return 0
    return row["total"]


def get_total_products():
    return count("SELECT COUNT(*) AS total FROM Produit")


def get_entry_voucher_count():
    return count("SELECT COUNT(*) AS total FROM BondeEntree")


def get_exit_voucher_count():
    return count("SELECT COUNT(*) AS total FROM BondeSortie")


def get_total_stock():
    return count("SELECT COALESCE(SUM(Stock), 0) AS total FROM Produit")


def get_total_entries():
    return count("SELECT COALESCE(SUM(QteEntree), 0) AS total FROM BondeEntree")


def get_total_exits():
    return count("SELECT COALESCE(SUM(QteSortie), 0) AS total FROM BondeSortie")


def get_dashboard_stats():
    """Retourne en une requête les indicateurs nécessaires au tableau de bord."""
    row = execute_one(
        "SELECT "
        "COUNT(*) AS total_products, "
        "COALESCE(SUM(Stock), 0) AS total_stock, "
        "COALESCE(SUM(Stock <= 0), 0) AS out_of_stock, "
        "COALESCE(SUM(Stock BETWEEN 1 AND 5), 0) AS low, "
        "COALESCE(SUM(Stock BETWEEN 6 AND 10), 0) AS medium, "
        "COALESCE(SUM(Stock > 10), 0) AS high, "
        "(SELECT COUNT(*) FROM BondeEntree) AS entry_vouchers, "
        "(SELECT COUNT(*) FROM BondeSortie) AS exit_vouchers "
        "FROM Produit"
    ) or {}

    return {
        "total_products": int(row.get("total_products") or 0),
        "total_stock": int(row.get("total_stock") or 0),
        "out_of_stock": int(row.get("out_of_stock") or 0),
        "low": int(row.get("low") or 0),
        "medium": int(row.get("medium") or 0),
        "high": int(row.get("high") or 0),
        "entry_vouchers": int(row.get("entry_vouchers") or 0),
        "exit_vouchers": int(row.get("exit_vouchers") or 0),
    }


def get_low_stock_products(limit=8):
    """Produits à surveiller, du stock le plus faible au plus élevé."""
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit "
        "ORDER BY Stock ASC, Design ASC, NumProduit ASC LIMIT %s",
        (limit,),
        fetch=True,
    )


def get_monthly_entry_vouchers():
    today = date.today()
    return count(
        "SELECT COUNT(*) AS total FROM BondeEntree "
        "WHERE YEAR(DateEntree) = %s AND MONTH(DateEntree) = %s",
        (today.year, today.month),
    )


def get_last_month_entry_vouchers():
    today = date.today()
    month, year = today.month, today.year
    if month == 1:
        month, year = 12, year - 1
    else:
        month -= 1
    return count(
        "SELECT COUNT(*) AS total FROM BondeEntree "
        "WHERE YEAR(DateEntree) = %s AND MONTH(DateEntree) = %s",
        (year, month),
    )


def stock_distribution():
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



def add_entry(num_voucher, num_product, qty, voucher_date):
    execute_many([
        (
            "INSERT INTO BondeEntree (NumBon, NumProduit, QteEntree, DateEntree) "
            "VALUES (%s, %s, %s, %s)",
            (num_voucher, num_product, qty, voucher_date),
        ),
        (
            "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
            (qty, num_product),
        ),
    ])



def add_exit(num_voucher, num_product, qty, voucher_date):
    product = get_product(num_product)
    if product is None:
        raise ValueError(f"Le produit '{num_product}' n'existe pas.")
    if int(product["Stock"]) < int(qty):
        raise ValueError(
            f"Stock insuffisant pour '{num_product}' : "
            f"{product['Stock']} disponible(s) pour une sortie de {qty}."
        )
    execute_many([
        (
            "INSERT INTO BondeSortie (NumBon, NumProduit, QteSortie, DateSortie) "
            "VALUES (%s, %s, %s, %s)",
            (num_voucher, num_product, qty, voucher_date),
        ),
        (
            "UPDATE Produit SET Stock = Stock - %s WHERE NumProduit = %s",
            (qty, num_product),
        ),
    ])
 

def update_entry(num_voucher, num_product, qty, voucher_date):
    line = execute_one(
        "SELECT NumProduit, QteEntree FROM BondeEntree WHERE NumBon = %s",
        (num_voucher,),
    )
    if line is None:
        raise ValueError(f"Le bon d'entrée '{num_voucher}' n'existe pas.")
    old_product = line["NumProduit"]
    old_qty = int(line["QteEntree"])
    new_qty = int(qty)
    if old_product == num_product:
        queries = [
            (
                "UPDATE BondeEntree SET QteEntree = %s, DateEntree = %s "
                "WHERE NumBon = %s AND NumProduit = %s",
                (new_qty, voucher_date, num_voucher, num_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock - %s + %s WHERE NumProduit = %s",
                (old_qty, new_qty, num_product),
            ),
        ]
    else:
        queries = [
            (
                "UPDATE BondeEntree SET NumProduit = %s, QteEntree = %s, "
                "DateEntree = %s WHERE NumBon = %s AND NumProduit = %s",
                (num_product, new_qty, voucher_date, num_voucher, old_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock - %s WHERE NumProduit = %s",
                (old_qty, old_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
                (new_qty, num_product),
            ),
        ]
    execute_many(queries)


def update_exit(num_voucher, num_product, qty, voucher_date):
    """Modification d'un bon de sortie : on n'applique que la différence au stock."""
    line = execute_one(
        "SELECT NumProduit, QteSortie FROM BondeSortie WHERE NumBon = %s",
        (num_voucher,),
    )
    if line is None:
        raise ValueError(f"Le bon de sortie '{num_voucher}' n'existe pas.")

    old_product = line["NumProduit"]
    old_qty = int(line["QteSortie"])
    new_qty = int(qty)

    if old_product == num_product:
        product = get_product(num_product)
        available = 0 if product is None else int(product["Stock"]) + old_qty
        if product is None or available < new_qty:
            raise ValueError(
                f"Stock insuffisant pour '{num_product}' : "
                f"{available} disponible(s) pour une sortie de {new_qty}."
            )
        queries = [
            (
                "UPDATE BondeSortie SET QteSortie = %s, DateSortie = %s "
                "WHERE NumBon = %s AND NumProduit = %s",
                (new_qty, voucher_date, num_voucher, num_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock + %s - %s WHERE NumProduit = %s",
                (old_qty, new_qty, num_product),
            ),
        ]
    else:
        product = get_product(num_product)
        if product is None or int(product["Stock"]) < new_qty:
            available = 0 if product is None else int(product["Stock"])
            raise ValueError(
                f"Stock insuffisant pour '{num_product}' : "
                f"{available} disponible(s) pour une sortie de {new_qty}."
            )
        queries = [
            (
                "UPDATE BondeSortie SET NumProduit = %s, QteSortie = %s, "
                "DateSortie = %s WHERE NumBon = %s AND NumProduit = %s",
                (num_product, new_qty, voucher_date, num_voucher, old_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
                (old_qty, old_product),
            ),
            (
                "UPDATE Produit SET Stock = Stock - %s WHERE NumProduit = %s",
                (new_qty, num_product),
            ),
        ]
    execute_many(queries)


def get_product(num_product):
    """Renvoie le produit demandé, ou None s'il n'existe pas."""
    return execute_one(
        "SELECT NumProduit, Design, Stock FROM Produit WHERE NumProduit = %s",
        (num_product,),
    )


def recent_movements(limit=12):
    movements = []

    for row in execute(
        "SELECT NumBon, NumProduit, QteEntree AS Quantity, DateEntree AS Day "
        "FROM BondeEntree ORDER BY DateEntree DESC, NumBon DESC LIMIT 50",
        fetch=True,
    ):
        movements.append(
            {
                "Day": row["Day"],
                "Direction": "ENTRY",
                "NumBon": row["NumBon"],
                "NumProduit": row["NumProduit"],
                "Quantity": row["Quantity"],
            }
        )

    for row in execute(
        "SELECT NumBon, NumProduit, QteSortie AS Quantity, DateSortie AS Day "
        "FROM BondeSortie ORDER BY DateSortie DESC, NumBon DESC LIMIT 50",
        fetch=True,
    ):
        movements.append(
            {
                "Day": row["Day"],
                "Direction": "EXIT",
                "NumBon": row["NumBon"],
                "NumProduit": row["NumProduit"],
                "Quantity": row["Quantity"],
            }
        )

    movements.sort(
        key=lambda movement: (movement["Day"], movement["NumBon"]),
        reverse=True,
    )
    return movements[:limit]


def add_product(num_product, designation, stock):
    execute(
        "INSERT INTO Produit (NumProduit, Design, Stock) VALUES (%s, %s, %s)",
        (num_product, designation, stock),
    )


def update_product(num_product, designation, stock):
    execute(
        "UPDATE Produit SET Design = %s, Stock = %s WHERE NumProduit = %s",
        (designation, stock, num_product),
    )
    
def delete_product(num_product):
    execute(
        "DELETE FROM Produit WHERE NumProduit = %s",
        (num_product,),
    )


def delete_exit(num_voucher, qty, num_product=None):
    if num_product is None:
        line = execute_one(
            "SELECT NumProduit FROM BondeSortie WHERE NumBon = %s",
            (num_voucher,),
        )
        if line is None:
            raise ValueError(f"Le bon de sortie '{num_voucher}' n'existe pas.")
        num_product = line["NumProduit"]
    execute_many([
        (
            "DELETE FROM BondeSortie WHERE NumBon = %s AND NumProduit = %s",
            (num_voucher, num_product),
        ),
        (
            "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
            (qty, num_product),
        ),
    ])




def delete_entry(num_voucher, qty, num_product=None):
    if num_product is None:
        line = execute_one(
            "SELECT NumProduit FROM BondeEntree WHERE NumBon = %s",
            (num_voucher,),
        )
        if line is None:
            raise ValueError(f"Le bon d'entrée '{num_voucher}' n'existe pas.")
        num_product = line["NumProduit"]
    execute_many([
        (
            "DELETE FROM BondeEntree WHERE NumBon = %s AND NumProduit = %s",
            (num_voucher, num_product),
        ),
        (
            "UPDATE Produit SET Stock = Stock - %s WHERE NumProduit = %s",
            (qty, num_product),
        ),
    ])



def _voucher_table(direction):
    """Nom de la table correspondant au sens (« ENTRY » ou « EXIT »)."""
    return TABLE_ENTRY if direction == "ENTRY" else TABLE_EXIT


def _qty_column(direction):
    """Nom de la colonne de quantité dans la table du bon."""
    return "QteEntree" if direction == "ENTRY" else "QteSortie"


def _date_column(direction):
    """Nom de la colonne de date dans la table du bon."""
    return "DateEntree" if direction == "ENTRY" else "DateSortie"


def _voucher_label(direction):
    return "d'entrée" if direction == "ENTRY" else "de sortie"


def _product_rows(direction, num_product, start, end):
    """Lignes de bons d'un produit, entre deux dates (facultatives)."""
    qty_column = _qty_column(direction)
    date_column = _date_column(direction)

    query = (
        f"SELECT NumBon, {qty_column} AS Quantity, {date_column} AS Day "
        f"FROM {_voucher_table(direction)} WHERE NumProduit = %s"
    )
    params = [num_product]

    if start is not None:
        query += f" AND {date_column} >= %s"
        params.append(start)

    if end is not None:
        query += f" AND {date_column} <= %s"
        params.append(end)

    query += f" ORDER BY {date_column}, NumBon"
    return execute(query, tuple(params), fetch=True)


def list_movements(num_product, start=None, end=None):
    movements = []

    for row in _product_rows("ENTRY", num_product, start, end):
        movements.append(
            {
                "Day": row["Day"],
                "NumBon": row["NumBon"],
                "Entry": row["Quantity"],
                "Exit": 0,
            }
        )

    for row in _product_rows("EXIT", num_product, start, end):
        movements.append(
            {
                "Day": row["Day"],
                "NumBon": row["NumBon"],
                "Entry": 0,
                "Exit": row["Quantity"],
            }
        )

    movements.sort(key=lambda movement: (movement["Day"], movement["NumBon"]))
    return movements


def movements_summary(num_product, start=None, end=None):
    """Retourne les mouvements et leurs totaux pour un produit."""
    movements = list_movements(num_product, start, end)
    return {
        "movements": movements,
        "total_entries": sum(movement["Entry"] or 0 for movement in movements),
        "total_exits": sum(movement["Exit"] or 0 for movement in movements),
    }
