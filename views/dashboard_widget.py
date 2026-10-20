from PySide6.QtWidgets import QWidget
from  ui_compiled.ui_dashboard_widget import Ui_dashboard
from  ui_compiled.ui_stock_widget import Ui_stockWidget
import db


class dashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        self.refresh()

    def init_count(self):
        total_stock = db.get_total_stock()
        total_products = db.get_total_products()
        nb_bons_entree = db.get_nb_bons_entree()
        nb_bons_sortie = db.get_nb_bons_sortie()
        self.ui.textTotalStock.setText(str(total_stock))
        self.ui.textTotalProduct.setText(str(total_products))
        self.ui.textTotalBondeEntree.setText(str(nb_bons_entree))
        self.ui.textTotalBondeSortie.setText(str(nb_bons_sortie))


    def refresh(self):
        self.init_count()
        produits = db.product_lists()
        self.ui.histogramme.set_data(
            [(produit["Design"], produit["Stock"]) for produit in produits]
        )
        self.ui.camembert.set_data(db.stock_repartition())


