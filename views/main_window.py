from PySide6.QtWidgets import QMainWindow

from ui_compiled.ui_main_window import Ui_StockIt
from views.dashboard_widget import DashboardWidget
from views.entry_widget import EntryWidget
from views.exit_widget import ExitWidget
from views.stock_widget import StockWidget
from views.movement_widget import MovementWidget
from views.product_widget import ProductWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StockIt()
        self.ui.setupUi(self)
        self.setWindowTitle("Stock IT")
        self.page_entry = EntryWidget()
        self.ui.stackedWidget.addWidget(self.page_entry)

        self.ui.entryBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.page_entry)
        )

        self.stock_widget = StockWidget()
        self.ui.stackedWidget.addWidget(self.stock_widget)

        self.ui.stockBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.stock_widget)
        )
        self.page_exit = ExitWidget()
        self.ui.stackedWidget.addWidget(self.page_exit)
        self.ui.sortieBtn.clicked.connect(
            lambda : self.ui.stackedWidget.setCurrentWidget(
                self.page_exit
            )
        )
        self.dashboard_window = DashboardWidget()
        self.ui.stackedWidget.addWidget(self.dashboard_window)

        self.ui.dashboardBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.dashboard_window)
        )
        self.product_widget = ProductWidget()
        self.ui.stackedWidget.addWidget(self.product_widget)

        self.ui.gestionBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.product_widget)
        )
        self.movement_widget = MovementWidget()
        self.ui.stackedWidget.addWidget(self.movement_widget)

        self.ui.mouvementBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.movement_widget)
        )

