from PySide6.QtWidgets import QDialog
from ui_compiled.ui_add_entry_dialog import Ui_Dialog


class AddEntryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Ajout d'un bon d'entrée")
    def get_dialog_data(self):
        return [
            self.ui.numBonInput.text(),
            self.ui.numProdInput.text(),
            self.ui.qteInput.value(),
            self.ui.dateInput.date().toString("yyyy-MM-dd") ,
        ]
    