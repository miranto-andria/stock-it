from PySide6.QtWidgets import QMainWindow
from ui_compiled.main_widget import Ui_Stock_It
from views.entry_widget import EntryWidget
class mainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.ui = Ui_Stock_It()
      self.ui.setupUi(self)
      self.page_entry = EntryWidget()
      self.ui.stackedWidget.addWidget(self.page_entry)


      self.ui.entryBtn.clicked.connect(
         lambda: self.ui.stackedWidget.setCurrentWidget(self.page_entry)
      )