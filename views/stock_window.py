from PySide6.QtWidgets import QWidget
from  ui_compiled.stock_widget import Ui_stockWidget
import db
class stockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_stockWidget()
        self.ui.setupUi(self)
        self.init_count()

    def init_count(self):
        total_stock = db.get_total_stock()
        total_products = db.get_total_products()
        self.ui.textTotalStock.setText(str(total_stock))
        self.ui.textTotalProduct.setText(str(total_products))

