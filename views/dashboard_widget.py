from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

import db
import resources_rc
from ui_compiled.ui_dashboard_widget import Ui_Dashboard

CARD_ICONS = {
    "tile_ico_produits": "product.png",
    "tile_ico_stock": "box.png",
    "tile_ico_entrees": "inward.png",
    "tile_ico_sorties": "outward.png",
}


def icon_pixmap(file_name, size=22):
    pixmap = QPixmap(f":/icons/{file_name}")
    return pixmap.scaled(
        size,
        size,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        for object_name, file_name in CARD_ICONS.items():
            getattr(self.ui, object_name).setPixmap(icon_pixmap(file_name))
        self.refresh()

    def init_count(self, stats):
        self.ui.valeur_stock.setText(str(stats["total_stock"]))
        self.ui.valeur_produits.setText(str(stats["total_products"]))
        self.ui.valeur_entrees.setText(str(stats["entry_vouchers"]))
        self.ui.valeur_sorties.setText(str(stats["exit_vouchers"]))
        self.ui.stats.setText(
            f"{stats['out_of_stock']} en rupture  |  {stats['low']} à surveiller  |  "
            f"{stats['medium']} niveau moyen  |  {stats['high']} niveau confortable"
        )

    def refresh(self):
        stats = {
            "total_products": 0,
            "total_stock": 0,
            "entry_vouchers": 0,
            "exit_vouchers": 0,
            "out_of_stock": 0,
            "low": 0,
            "medium": 0,
            "high": 0,
        }
        products = []
        movements = []
        try:
            stats.update(db.get_dashboard_stats() or {})
            products = db.get_low_stock_products() or []
            movements = db.recent_movements(12) or []
        except Exception:
            pass
        self.init_count(stats)
        self.ui.histogramme.set_data(
            [(product["Design"], product["Stock"]) for product in products]
        )
        self.ui.camembert.set_data(
            [
                ("Rupture", stats["out_of_stock"]),
                ("Faible", stats["low"]),
                ("Moyen", stats["medium"]),
                ("Confortable", stats["high"]),
            ]
        )
        self.ui.derniers_mouvements.clear()
        for movement in movements:
            is_entry = movement["Direction"] == "ENTRY"
            sign = "+" if is_entry else "-"
            word = "ENTRÉE" if is_entry else "SORTIE"
            self.ui.derniers_mouvements.addItem(
                f"{movement['Day'].strftime('%d/%m/%Y')}   {word:<6} "
                f"{movement['NumBon']} - {movement['NumProduit']} "
                f": {sign}{movement['Quantity']}"
            )
        if not movements:
            self.ui.derniers_mouvements.addItem("- aucun mouvement enregistré -")
