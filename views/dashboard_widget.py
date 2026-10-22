from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget

import db
import resources_rc
from db import get_total_products, get_total_stock
from ui_compiled.ui_dashboard_widget import Ui_Dashboard

ICONES_PAR_CARTE = {
    "tile_ico_produits": "product.svg",
    "tile_ico_stock": "box.svg",
    "tile_ico_entrees": "inward.svg",
    "tile_ico_sorties": "outward.svg",
}


def icone_pixmap(nom_fichier, taille=22):
    rendu = QSvgRenderer(f":/icons/{nom_fichier}")
    image = QImage(taille, taille, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    peintre = QPainter(image)
    peintre.setRenderHint(QPainter.RenderHint.Antialiasing)
    peintre.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
    rendu.render(peintre, QRectF(0, 0, taille, taille))
    peintre.end()
    return QPixmap.fromImage(image)


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        for nom_objet, nom_fichier in ICONES_PAR_CARTE.items():
            getattr(self.ui, nom_objet).setPixmap(icone_pixmap(nom_fichier))
        self.refresh()

    def init_count(self):
        total_stock = db.get_total_stock()
        total_products = db.get_total_products()
        nb_bons_entree = db.get_nb_bons_entree()
        nb_bons_sortie = db.get_nb_bons_sortie()
        self.ui.valeur_stock.setText(str(total_stock))
        self.ui.valeur_produits.setText(str(total_products))
        self.ui.valeur_entrees.setText(str(nb_bons_entree))
        self.ui.valeur_sorties.setText(str(nb_bons_sortie))
        repartition = dict(db.stock_repartition())
        rupture = repartition["Rupture(0)"]
        faible = repartition["Faible(1-5)"]
        moyen = repartition["Moyen(6-10)"]
        eleve = repartition["Élevé(> 10)"]
        self.ui.stats.setText(
            f"{get_total_products()} produits - {get_total_stock()} unités "
            f"- {rupture} en rupture - {faible} stock faible"
            f"- {moyen} Moyen - {eleve} Élevé"
        )

    def refresh(self):
        self.init_count()
        produits = db.product_lists()
        self.ui.histogramme.set_data(
            [(produit["Design"], produit["Stock"]) for produit in produits]
        )
        self.ui.camembert.set_data(db.stock_repartition())
        self.ui.derniers_mouvements.clear()
        mouvements = db.derniers_mouvements(12)
        for mouvement in mouvements:
            entre = mouvement["Sens"] == "ENTREE"
            signe = "+" if entre else "-"
            mot = "ENTRÉE" if entre else "SORTIE"
            self.ui.derniers_mouvements.addItem(
                f"{mouvement['Jour'].strftime('%d/%m/%Y')}   {mot:<6} "
                f"{mouvement['NumBon']} - {mouvement['NumProduit']} "
                f": {signe}{mouvement['Quantite']}"
            )
        if not mouvements:
            self.ui.derniers_mouvements.addItem("- aucun mouvement enregistré -")
