from PySide6.QtWidgets import QWidget
from  ui_compiled.ui_stock_widget import Ui_stockWidget
import db
import  utils.table_management as tbm
import utils.pdf_export
from utils import pdf_export


class stockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_stockWidget()
        self.ui.setupUi(self)
        tbm.columns_setting(self.ui.table, [160, 0, 110], colonne_etirable=1)
        self.ui.table.verticalHeader().setVisible(False)
        self.ui.btnPdf.clicked.connect(lambda : pdf_export.from_table(self, self.ui.table))
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
        self.ui.btnSearch.clicked.connect(self.refresh)


    def refresh(self):
        self.init_count()
        produits = db.search_product(self.ui.search.text())
        tbm.fill_table(
            self.ui.table,
            [
                [produit["NumProduit"], produit["Design"], produit["Stock"]]
                for produit in produits
            ],
        )
        self.ui.histogramme.set_data(
            [(produit["Design"], produit["Stock"]) for produit in produits]
        )
        self.ui.camembert.set_data(db.stock_repartition())


