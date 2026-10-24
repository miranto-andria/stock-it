from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

import db
import resources_rc
from ui_compiled.ui_dashboard_widget import Ui_Dashboard

ICONES_PAR_CARTE = {
    "tile_ico_produits": "product.png",
    "tile_ico_stock": "box.png",
    "tile_ico_entrees": "inward.png",
    "tile_ico_sorties": "outward.png",
}


def icone_pixmap(nom_fichier, taille=22):
    pixmap = QPixmap(f":/icons/{nom_fichier}")
    return pixmap.scaled(
        taille,
        taille,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        for nom_objet, nom_fichier in ICONES_PAR_CARTE.items():
            getattr(self.ui, nom_objet).setPixmap(icone_pixmap(nom_fichier))
        self.refresh()

    def init_count(self, stats):
        self.ui.valeur_stock.setText(str(stats["total_stock"]))
        self.ui.valeur_produits.setText(str(stats["total_products"]))
        self.ui.valeur_entrees.setText(str(stats["bons_entree"]))
        self.ui.valeur_sorties.setText(str(stats["bons_sortie"]))
        self.ui.stats.setText(
            f"{stats['rupture']} en rupture  |  {stats['faible']} à surveiller  |  "
            f"{stats['moyen']} niveau moyen  |  {stats['eleve']} niveau confortable"
        )

    def refresh(self):
        stats = {
            "total_products": 0,
            "total_stock": 0,
            "bons_entree": 0,
            "bons_sortie": 0,
            "rupture": 0,
            "faible": 0,
            "moyen": 0,
            "eleve": 0,
        }
        produits = []
        mouvements = []
        try:
            stats.update(db.get_dashboard_stats() or {})
            produits = db.get_low_stock_products() or []
            mouvements = db.derniers_mouvements(12) or []
        except Exception:
            # Les widgets restent utilisables si la base est indisponible.
            pass
        self.init_count(stats)
        self.ui.histogramme.set_data(
            [(produit["Design"], produit["Stock"]) for produit in produits]
        )
        self.ui.camembert.set_data(
            [
                ("Rupture", stats["rupture"]),
                ("Faible", stats["faible"]),
                ("Moyen", stats["moyen"]),
                ("Confortable", stats["eleve"]),
            ]
        )
        self.ui.derniers_mouvements.clear()
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
