from PySide6.QtWidgets import QMainWindow
from ui_compiled.main_widget import Ui_Stock_It
from views.stock_window import stockWindow

class mainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.ui = Ui_Stock_It()
      self.ui.setupUi(self)
      self.stock_window = stockWindow()
      self.ui.stackedWidget.addWidget(self.stock_window)
      self.ui.stockBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.stock_window))