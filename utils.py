from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QMessageBox, QTableWidgetItem


def fill_table(table, lignes):
    tri_actif = table.isSortingEnabled()
    table.setSortingEnabled(False)
    table.setRowCount(0)
    for valeurs in lignes:
        ligne = table.rowCount()
        table.insertRow(ligne)
        for colonne, valeur in enumerate(valeurs):
            if valeur is None:
                texte = ""
            elif isinstance(valeur, float) and valeur.is_integer():
                texte = str(int(valeur))
            else:
                texte = str(valeur)
            item = QTableWidgetItem(texte)
            if colonne and isinstance(valeur, (int, float)) and not isinstance(valeur, bool):
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            else:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            table.setItem(ligne, colonne, item)
    table.setSortingEnabled(tri_actif)

def columns_setting(table, largeurs, colonne_etirable):
    for colonne, largeur in enumerate(largeurs):
        if largeur:
            table.setColumnWidth(colonne, largeur)
    table.horizontalHeader().setSectionResizeMode(
        colonne_etirable, QHeaderView.ResizeMode.Stretch
    )