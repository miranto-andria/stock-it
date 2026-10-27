from PySide6.QtWidgets import QDialog
from ui_compiled.ui_add_exit_dialog import Ui_ExitDialog


class AddExitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExitDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Ajout d'un bon de sortie")
    def get_dialog_data(self):
        return [
            self.ui.numBonInput.text(),
            self.ui.numProdInput.text(),
            self.ui.qteInput.value(),
            self.ui.dateInput.date().toString("yyyy-MM-dd") ,
        ]
    