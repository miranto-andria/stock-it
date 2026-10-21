
from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_product_widget import Ui_productWidget
import db
from views.entry_dialog import AddEntryDialog
from ui_compiled.ui_add_entry_dialog import Ui_Dialog
from utils.table_management import fill_table
import utils.table_management as tbm
class ProductWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_productWidget()
        self.ui.setupUi(self)
        tbm.columns_setting(self.ui.productTable, [160, 0, 110], colonne_etirable=1)
        self.ui.productTable.verticalHeader().setVisible(False)
        self.set_product_table()
    def set_product_table(self):
        produits = db.product_lists()
        tbm.fill_table(
        self.ui.productTable,
        [
            [produit["NumProduit"], produit["Design"], produit["Stock"]]
                for produit in produits
            ],
        )


  