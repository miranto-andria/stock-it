
from PySide6.QtWidgets import QMainWindow
from ui_compiled.ui_main_window import Ui_Stock_It
from views.dashboard_widget import dashboardWindow
from views.entry_widget import EntryWidget
from views.stock_widget import StockWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Stock_It()
        self.ui.setupUi(self)

        self.page_entry = EntryWidget()
        self.ui.stackedWidget.addWidget(self.page_entry)

        self.ui.entryBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.page_entry
            )
        )

        self.stock_window = StockWidget()
        self.ui.stackedWidget.addWidget(self.stock_window)

        self.ui.stockBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.stock_window
            )
        )
        self.dashboard_window = dashboardWindow()
        self.ui.stackedWidget.addWidget(self.dashboard_window)

        self.ui.dashboardBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.dashboard_window
            )
        )
