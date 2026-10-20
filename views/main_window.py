
from PySide6.QtWidgets import QMainWindow
from ui_compiled.ui_main_widget import Ui_Stock_It
from views.entry_widget import EntryWidget
from views.stock_window import stockWindow


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Stock_It()
        self.ui.setupUi(self)

        # Page des entrées
        self.page_entry = EntryWidget()
        self.ui.stackedWidget.addWidget(self.page_entry)

        self.ui.entryBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.page_entry
            )
        )

        # Page du stock
        self.stock_window = stockWindow()
        self.ui.stackedWidget.addWidget(self.stock_window)

        self.ui.stockBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.stock_window
            )
        )
