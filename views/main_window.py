from PySide6.QtWidgets import QMainWindow
from ui_compiled.main_widget import Ui_Stock_It

class mainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.ui = Ui_Stock_It()
      self.ui.setupUi(self)