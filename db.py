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

def get_total_stock():
    total_stock = execute("SELECT SUM(Stock) as total_stock from produit", fetch=True)
    return total_stock[0]["total_stock"]

def get_total_products():
    product_count = execute("SELECT COUNT(NumProduit) as total_products FROM produit" , fetch=True)
    return product_count[0]["total_products"]