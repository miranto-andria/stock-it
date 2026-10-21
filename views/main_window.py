
from PySide6.QtWidgets import QMainWindow
from ui_compiled.ui_main_widget import Ui_Stock_It
from views.entry_widget import EntryWidget
from views.stock_widget import stockWidget
from views.product_widget import ProductWidget


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Stock_It()
        self.ui.setupUi(self)
        self.setWindowTitle("Stock IT")
        # Page des entrées
        self.page_entry = EntryWidget()
        self.ui.stackedWidget.addWidget(self.page_entry)

        self.ui.entryBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.page_entry
            )
        )

        # Page du stock
        self.stock_widget = stockWidget()
        self.ui.stackedWidget.addWidget(self.stock_widget)

        self.ui.stockBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.stock_widget
            )
        )
        self.product_widget = ProductWidget()
        self.ui.stackedWidget.addWidget(self.product_widget)
        
        self.ui.gestionBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
            self.product_widget
        )
        )
