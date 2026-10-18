
from datetime import datetime

from PySide6.QtCore import Qt, QRectF, QMarginsF
from PySide6.QtGui import (
    QPdfWriter,
    QPainter,
    QFont,
    QColor,
    QPen,
    QPageSize,
    QPageLayout,
)
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase

def load_montserrat():
    fonts_dir = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "fonts"
    )

    for fichier in fonts_dir.glob("*.ttf"):
        QFontDatabase.addApplicationFont(str(fichier))
        
def from_table(parent, table):
    load_montserrat()
    chemin, _ = QFileDialog.getSaveFileName(
        parent,
        "Exporter le stock en PDF",
        "Stock_IT_rapport.pdf",
        "Fichiers PDF (*.pdf)"
    )

    if not chemin:
        return

    if not chemin.lower().endswith(".pdf"):
        chemin += ".pdf"

    try:
        entetes = []
        for colonne in range(table.columnCount()):
            item = table.horizontalHeaderItem(colonne)
            entetes.append(
                item.text() if item else f"Colonne {colonne + 1}"
            )

        donnees = []
        for ligne in range(table.rowCount()):
            if table.isRowHidden(ligne):
                continue

            valeurs = []
            for colonne in range(table.columnCount()):
                item = table.item(ligne, colonne)
                valeurs.append(item.text() if item else "")

            donnees.append(valeurs)

        if not entetes:
            QMessageBox.warning(
                parent, "Stock IT", "Le tableau ne contient aucune colonne."
            )
            return

        pdf = QPdfWriter(chemin)
        pdf.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
        pdf.setPageOrientation(QPageLayout.Orientation.Landscape)
        pdf.setResolution(96)
        pdf.setTitle("Stock IT - Rapport de stock")
        pdf.setCreator("Stock IT")

        marges = QMarginsF(12, 15, 12, 15)
        pdf.setPageMargins(marges, QPageLayout.Unit.Millimeter)

        painter = QPainter()
        if not painter.begin(pdf):
            raise RuntimeError("Impossible de démarrer la création du PDF.")

        try:
            largeur = pdf.width()
            hauteur = pdf.height()

            violet = QColor("#6243FF")
            fond = QColor("#13141F")
            texte = QColor("#252638")
            texte_clair = QColor("#FFFFFF")
            ligne_couleur = QColor("#D9D9E5")
            fond_pair = QColor("#F1F2F8")
            fond_impair = QColor("#FFFFFF")

            marge_gauche = 0
            marge_droite = largeur
            y = 0
            page = 1

            hauteur_titre = 42
            hauteur_sous_titre = 25
            hauteur_entete = 32
            hauteur_ligne = 28
            hauteur_pied = 24

            def design_header():
                nonlocal y

                painter.fillRect(
                    QRectF(0, 0, largeur, hauteur_titre + 10),
                    fond
                )

                painter.setPen(texte_clair)
                painter.setFont(QFont("Montserrat", 17, QFont.Weight.Bold))
                painter.drawText(
                    QRectF(12, 5, largeur - 24, 28),
                    Qt.AlignmentFlag.AlignVCenter,
                    "STOCK IT"
                )

                painter.setFont(QFont("Montserrat", 9))
                painter.setPen(QColor("#C5C6D8"))
                painter.drawText(
                    QRectF(12, 32, largeur - 24, 18),
                    Qt.AlignmentFlag.AlignVCenter,
                    "Rapport de stock - "
                    + datetime.now().strftime("%d/%m/%Y à %H:%M")
                )

                y = hauteur_titre + hauteur_sous_titre

            def design_footer():
                painter.setPen(QPen(violet, 1.5))
                painter.drawLine(
                    0, hauteur - hauteur_pied,
                    largeur, hauteur - hauteur_pied
                )
                painter.setPen(QColor("#77788D"))
                painter.setFont(QFont("Montserrat", 8))
                painter.drawText(
                    QRectF(0, hauteur - hauteur_pied + 3, largeur, 18),
                    Qt.AlignmentFlag.AlignCenter,
                    f"Stock IT | Page {page}"
                )

            def design_cell_row(valeurs, y_ligne, hauteur, entete=False, index=0):
                nb_colonnes = len(entetes)
                largeur_colonne = largeur / nb_colonnes

                for colonne, valeur in enumerate(valeurs):
                    x = colonne * largeur_colonne
                    rect = QRectF(
                        x, y_ligne, largeur_colonne, hauteur
                    )

                    if entete:
                        couleur_fond = violet
                        couleur_texte = texte_clair
                        police = QFont("Montserrat", 9, QFont.Weight.Bold)
                    else:
                        couleur_fond = (
                            fond_pair if index % 2 == 0 else fond_impair
                        )
                        couleur_texte = texte
                        police = QFont("Montserrat", 9)

                    painter.fillRect(rect, couleur_fond)
                    painter.setPen(QPen(ligne_couleur, 0.7))
                    painter.drawRect(rect)

                    painter.setPen(couleur_texte)
                    painter.setFont(police)

                    texte_cellule = painter.fontMetrics().elidedText(
                        str(valeur),
                        Qt.TextElideMode.ElideRight,
                        max(10, int(largeur_colonne - 12))
                    )

                    painter.drawText(
                        rect.adjusted(6, 2, -6, -2),
                        Qt.AlignmentFlag.AlignVCenter
                        | Qt.AlignmentFlag.AlignLeft,
                        texte_cellule
                    )

            design_header()
            design_cell_row(entetes, y, hauteur_entete, entete=True)
            y += hauteur_entete

            for index, valeurs in enumerate(donnees):
                if y + hauteur_ligne > hauteur - hauteur_pied:
                    design_footer()
                    pdf.newPage()
                    page += 1
                    design_header()
                    design_cell_row(
                        entetes, y, hauteur_entete, entete=True
                    )
                    y += hauteur_entete

                design_cell_row(
                    valeurs, y, hauteur_ligne, index=index
                )
                y += hauteur_ligne

            design_footer()

        finally:
            painter.end()

        QMessageBox.information(
            parent,
            "Stock IT",
            f"Export PDF réussi :\n{chemin}"
        )

    except Exception as erreur:
        QMessageBox.critical(
            parent,
            "Erreur d'export",
            f"Impossible de générer le PDF :\n{erreur}"
        )
