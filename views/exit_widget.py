from PySide6.QtWidgets import QWidget , QTableWidgetItem
from ui_compiled.ui_exit_widget import Ui_exitWidget
from db import get_entry_pass

class ExitWidget(QWidget):
   def __init__(self):
        super().__init__()

        self.ui = Ui_exitWidget()
        self.ui.setupUi(self)
        
        