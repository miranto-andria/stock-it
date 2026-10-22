from PySide6.QtWidgets import QWidget
from  ui_compiled.ui_stock_widget import Ui_stockWidget
import db
import  utils.table_management as tbm
from utils import pdf_export


class StockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_stockWidget()
        self.ui.setupUi(self)
        tbm.columns_setting(self.ui.table, [160, 0, 110], colonne_etirable=1)
        self.ui.table.verticalHeader().setVisible(False)
        self.ui.btnPdf.clicked.connect(lambda : pdf_export.from_table(self, self.ui.table))
        self.refresh()
        self.ui.btnSearch.clicked.connect(self.refresh)



    def refresh(self):
        produits = db.search_product(self.ui.search.text())
        tbm.fill_table(
            self.ui.table,
            [
                [produit["NumProduit"], produit["Design"], produit["Stock"]]
                for produit in produits
            ],
        )


