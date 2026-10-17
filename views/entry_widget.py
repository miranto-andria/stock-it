
from PySide6.QtWidgets import QWidget
from ui_compiled.ui_entry_widget import Ui_entryWidget


class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_entryWidget()
        self.ui.setupUi(self)
