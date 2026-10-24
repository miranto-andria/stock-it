from datetime import date

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "stock_it",
}
TABLE_PRODUIT = "Produit"
TABLE_ENTREE = "BondeEntree"
TABLE_SORTIE = "BondeSortie"


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


def get_total_entrees():
    return count("SELECT COALESCE(SUM(QteEntree), 0) AS total FROM BondeEntree")


def get_total_sorties():
    return count("SELECT COALESCE(SUM(QteSortie), 0) AS total FROM BondeSortie")


def get_dashboard_stats():
    """Retourne en une requête les indicateurs nécessaires au tableau de bord."""
    ligne = execute_one(
        "SELECT "
        "COUNT(*) AS total_products, "
        "COALESCE(SUM(Stock), 0) AS total_stock, "
        "COALESCE(SUM(Stock <= 0), 0) AS rupture, "
        "COALESCE(SUM(Stock BETWEEN 1 AND 5), 0) AS faible, "
        "COALESCE(SUM(Stock BETWEEN 6 AND 10), 0) AS moyen, "
        "COALESCE(SUM(Stock > 10), 0) AS eleve, "
        "(SELECT COUNT(*) FROM BondeEntree) AS bons_entree, "
        "(SELECT COUNT(*) FROM BondeSortie) AS bons_sortie "
        "FROM Produit"
    ) or {}

    return {
        "total_products": int(ligne.get("total_products") or 0),
        "total_stock": int(ligne.get("total_stock") or 0),
        "rupture": int(ligne.get("rupture") or 0),
        "faible": int(ligne.get("faible") or 0),
        "moyen": int(ligne.get("moyen") or 0),
        "eleve": int(ligne.get("eleve") or 0),
        "bons_entree": int(ligne.get("bons_entree") or 0),
        "bons_sortie": int(ligne.get("bons_sortie") or 0),
    }


def get_low_stock_products(limite=8):
    """Produits à surveiller, du stock le plus faible au plus élevé."""
    return execute(
        "SELECT NumProduit, Design, Stock FROM Produit "
        "ORDER BY Stock ASC, Design ASC, NumProduit ASC LIMIT %s",
        (limite,),
        fetch=True,
    )


def get_bons_entree_mois():
    aujourdhui = date.today()
    return count(
        "SELECT COUNT(*) AS total FROM BondeEntree "
        "WHERE YEAR(DateEntree) = %s AND MONTH(DateEntree) = %s",
        (aujourdhui.year, aujourdhui.month),
    )


def get_bons_entree_mois_dernier():
    aujourdhui = date.today()
    mois, annee = aujourdhui.month, aujourdhui.year
    if mois == 1:
        mois, annee = 12, annee - 1
    else:
        mois -= 1
    return count(
        "SELECT COUNT(*) AS total FROM BondeEntree "
        "WHERE YEAR(DateEntree) = %s AND MONTH(DateEntree) = %s",
        (annee, mois),
    )


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


def add_entry(NumBon, NumProduit, QteEntree, Date):
    execute(
        "INSERT INTO BondeEntree (NumBon, NumProduit, QteEntree, DateEntree) "
        "VALUES (%s, %s, %s, %s)",
        (NumBon, NumProduit, QteEntree, Date),
    )
    execute(
        "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
        (QteEntree, NumProduit),
    )


def delete_product(numProduit):
    execute(
        "DELETE FROM Produit WHERE NumProduit = %s",
        (numProduit,),
    )

def update_entry(NumBon, NumProduit, QteEntree, DateEntree):
    execute(
        "UPDATE BondeEntree SET NumProduit = %s, QteEntree = %s, "
        "DateEntree = %s WHERE NumBon = %s",
        (NumProduit, QteEntree, DateEntree, NumBon),
    )


def produit(num_produit):
    """Renvoie le produit demandé, ou None s'il n'existe pas."""
    return execute_one(
        "SELECT NumProduit, Design, Stock FROM Produit WHERE NumProduit = %s",
        (num_produit,),
    )


def derniers_mouvements(limite=12):
    mouvements = []

    for ligne in execute(
        "SELECT NumBon, NumProduit, QteEntree AS Quantite, DateEntree AS Jour "
        "FROM BondeEntree ORDER BY DateEntree DESC, NumBon DESC LIMIT 50",
        fetch=True,
    ):
        mouvements.append(
            {
                "Jour": ligne["Jour"],
                "Sens": "ENTREE",
                "NumBon": ligne["NumBon"],
                "NumProduit": ligne["NumProduit"],
                "Quantite": ligne["Quantite"],
            }
        )

    for ligne in execute(
        "SELECT NumBon, NumProduit, QteSortie AS Quantite, DateSortie AS Jour "
        "FROM BondeSortie ORDER BY DateSortie DESC, NumBon DESC LIMIT 50",
        fetch=True,
    ):
        mouvements.append(
            {
                "Jour": ligne["Jour"],
                "Sens": "SORTIE",
                "NumBon": ligne["NumBon"],
                "NumProduit": ligne["NumProduit"],
                "Quantite": ligne["Quantite"],
            }
        )

    mouvements.sort(
        key=lambda mouvement: (mouvement["Jour"], mouvement["NumBon"]),
        reverse=True,
    )
    return mouvements[:limite]


def add_product(NumProduit, Designation, Stock):
    execute(
        "INSERT INTO Produit (NumProduit, Design, Stock) VALUES (%s, %s, %s)",
        (NumProduit, Designation, Stock),
    )


def delete_entry(numBon, QteSortie, NumProduit):
    execute("DELETE FROM BondeSortie WHERE NumBon = %s", [numBon])
    execute(
        "UPDATE Produit SET Stock = Stock + %s WHERE NumProduit = %s",
        (QteSortie, NumProduit),
    )


def update_product(NumProduit, Designation, Stock):
    execute(
        "UPDATE Produit SET Design = %s, Stock = %s WHERE NumProduit = %s",
        (Designation, Stock, NumProduit),
    )


def _table_bon(sens):
    """Nom de la table correspondant au sens (« ENTREE » ou « SORTIE »)."""
    return TABLE_ENTREE if sens == "ENTREE" else TABLE_SORTIE


def _colonne_quantite(sens):
    """Nom de la colonne de quantité dans la table du bon."""
    return "QteEntree" if sens == "ENTREE" else "QteSortie"


def _colonne_date(sens):
    """Nom de la colonne de date dans la table du bon."""
    return "DateEntree" if sens == "ENTREE" else "DateSortie"


def _libelle_bon(sens):
    return "d'entrée" if sens == "ENTREE" else "de sortie"


def _lignes_produit(sens, num_produit, debut, fin):
    """Lignes de bons d'un produit, entre deux dates (facultatives)."""
    colonne_qte = _colonne_quantite(sens)
    colonne_date = _colonne_date(sens)

    requete = (
        f"SELECT NumBon, {colonne_qte} AS Quantite, {colonne_date} AS Jour "
        f"FROM {_table_bon(sens)} WHERE NumProduit = %s"
    )
    parametres = [num_produit]

    if debut is not None:
        requete += f" AND {colonne_date} >= %s"
        parametres.append(debut)

    if fin is not None:
        requete += f" AND {colonne_date} <= %s"
        parametres.append(fin)

    requete += f" ORDER BY {colonne_date}, NumBon"
    return execute(requete, tuple(parametres), fetch=True)


def liste_mouvements(num_produit, debut=None, fin=None):
    mouvements = []

    for ligne in _lignes_produit("ENTREE", num_produit, debut, fin):
        mouvements.append(
            {
                "Jour": ligne["Jour"],
                "NumBon": ligne["NumBon"],
                "Entree": ligne["Quantite"],
                "Sortie": 0,
            }
        )

    for ligne in _lignes_produit("SORTIE", num_produit, debut, fin):
        mouvements.append(
            {
                "Jour": ligne["Jour"],
                "NumBon": ligne["NumBon"],
                "Entree": 0,
                "Sortie": ligne["Quantite"],
            }
        )

    mouvements.sort(key=lambda mouvement: (mouvement["Jour"], mouvement["NumBon"]))
    return mouvements


def resume_mouvements(num_produit, debut=None, fin=None):
    """Retourne les mouvements et leurs totaux pour un produit."""
    mouvements = liste_mouvements(num_produit, debut, fin)
    return {
        "mouvements": mouvements,
        "total_entree": sum(mouvement["Entree"] or 0 for mouvement in mouvements),
        "total_sortie": sum(mouvement["Sortie"] or 0 for mouvement in mouvements),
    }
