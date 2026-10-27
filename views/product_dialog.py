from PySide6.QtWidgets import QDialog
from ui_compiled.ui_add_product_dialog import Ui_ProdDialog


class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProdDialog()
        self.ui.setupUi(self)

    def get_dialog_data(self):
        return [
            self.ui.numProdInput.text(),
            self.ui.designationInput.text(),
            self.ui.stockInput.value() ,
        ]
