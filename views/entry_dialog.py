from PySide6.QtWidgets import QDialog
from ui_compiled.ui_add_entry_dialog import Ui_Dialog


class AddEntryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
    def get_dialog_data(self):
        return [
            self.ui.numBonInput.text(),
            self.ui.numProdInput.text(),
            self.ui.qteInput.text(),
            self.ui.dateInput.text(),
        ]
    