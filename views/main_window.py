
from PySide6.QtWidgets import QMainWindow
from ui_compiled.ui_main_window import Ui_Stock_It
from views.dashboard_widget import dashboardWindow
from views.entry_widget import EntryWidget

from views.stock_widget import StockWidget
from views.product_widget import ProductWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Stock_It()
        self.ui.setupUi(self)
        self.setWindowTitle("Stock IT")
        self.page_entry = EntryWidget()
        self.ui.stackedWidget.addWidget(self.page_entry)

        self.ui.entryBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.page_entry
            )
        )

        self.stock_widget = StockWidget()
        self.ui.stackedWidget.addWidget(self.stock_widget)

        self.ui.stockBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.stock_widget
            )
        )
        self.dashboard_window = dashboardWindow()
        self.ui.stackedWidget.addWidget(self.dashboard_window)

        self.ui.dashboardBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.dashboard_window
            )
        )
        self.product_widget = ProductWidget()
        self.ui.stackedWidget.addWidget(self.product_widget)
        
        self.ui.gestionBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
            self.product_widget
        )
        )
