

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_StockIt(object):
    def setupUi(self, Stock_It):
        if not Stock_It.objectName():
            Stock_It.setObjectName(u"Stock_It")
        Stock_It.resize(1280, 720)
        Stock_It.setStyleSheet(u"#sideBar{\n"
"background-color : #2563eb;\n"
"border-right : 1px solid rgba(255,255,255,0.25);\n"
"color : #ffffff\n"
"}\n"
"#centralwidget{\n"
"background : #f5f7f9;\n"
"}\n"
"\n"
"#sideBar QPushButton{\n"
"text-align : left;\n"
"border : none;\n"
"margin : 2px 10px;\n"
"padding : 11px 14px;\n"
"border-radius : 8px;\n"
"font-size : 10.5pt;\n"
"background-color : transparent;\n"
"color : #ffffff\n"
"}\n"
"#sideBar QPushButton:hover{\n"
"background-color : rgba(255,255,255,0.15);\n"
"color : #ffffff\n"
"}\n"
"#titleContainer{\n"
"margin-bottom : 24px;\n"
"}\n"
"\n"
"#title{\n"
"font-size : 26px;\n"
"font-weight : bold;\n"
"color : #ffffff\n"
"}\n"
"#mainSection, #mainSection #stackedWidget{\n"
"background-color : #f5f7f9\n"
"}\n"
"\n"
"QWidget {\n"
"    font-family: \"Montserrat\", \"Segoe UI\", sans-serif;\n"
"    color: #111827;\n"
"}\n"
"QMainWindow, QDialog, QMessageBox {\n"
"    background: #f5f7f9;\n"
"}\n"
"QStackedWidget, QScrollArea {\n"
"    background: #f5f7f9;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    back"
                        "ground: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"    margin-top: 14px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #2d66e4;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background: #ffffff;\n"
"    alternate-background-color: #f8f8f8;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 8px;\n"
"    gridline-color: #eef0f3;\n"
"    selection-background-color: #e8effc;\n"
"    selection-color: #111827;\n"
"    outline: none;\n"
"}\n"
"QHeaderView::section {\n"
"    background: rgba(45, 102, 228, 0.08);\n"
"    color: #2d66e4;\n"
"    padding: 8px 4px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #dfe7f7;\n"
"    font-weight: bold;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 6px 8px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background: #e8effc;\n"
"    color: #111827;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background: #f5f"
                        "7f9;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 7px 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: #f5f7f9;\n"
"    border-color: #abadae;\n"
"\n"
"    color: #111827;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #eef0f3;\n"
"}\n"
"QPushButton:focus {\n"
"    border: 1px solid #2d66e4;\n"
"}\n"
"QPushButton:disabled {\n"
"    color: #abadae;\n"
"    background: #f8f8f8;\n"
"    border-color: #e5e7eb;\n"
"}\n"
"\n"
"QPushButton[primaire=\"true\"] {\n"
"    background: #2d66e4;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2d66e4;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton[primaire=\"true\"]:hover {\n"
"    background: #2456c6;\n"
"}\n"
"QPushButton[primaire=\"true\"]:pressed {\n"
"    background: #1c46a5;\n"
"}\n"
"\n"
"QPushButton[accent=\"true\"] {\n"
"    background: #2d66e4;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2d66e4;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton[accent=\"true\"]:hover {\n"
"    background: #24"
                        "56c6;\n"
"}\n"
"QPushButton[accent=\"true\"]:pressed {\n"
"    background: #1c46a5;\n"
"}\n"
"\n"
"QPushButton[danger=\"true\"] {\n"
"    background: #dc4a4a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #dc4a4a;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton[danger=\"true\"]:hover {\n"
"    background: #c83d3d;\n"
"    border-color: #c83d3d;\n"
"}\n"
"QPushButton[danger=\"true\"]:pressed {\n"
"    background: #ad3030;\n"
"    border-color: #ad3030;\n"
"}\n"
"\n"
"QPushButton[success=\"true\"] {\n"
"    background: #15803d;\n"
"    color: #ffffff;\n"
"    border: 1px solid #15803d;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton[success=\"true\"]:hover {\n"
"    background: #126b34;\n"
"}\n"
"\n"
"QPushButton[secondary=\"true\"] {\n"
"    background: #ffffff;\n"
"    color: #374151;\n"
"    border: 1px solid #d5dbe3;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton[secondary=\"true\"]:hover {\n"
"    background: #eef3fb;\n"
"    border-color: #b8c7df;\n"
"}\n"
"\n"
"QPushButton[primaire=\"true\"]:disabl"
                        "ed,\n"
"QPushButton[accent=\"true\"]:disabled,\n"
"QPushButton[danger=\"true\"]:disabled {\n"
"    background: #f8f8f8;\n"
"    color: #abadae;\n"
"    border: 1px solid #e5e7eb;\n"
"}\n"
"QPushButton[success=\"true\"]:disabled,\n"
"QPushButton[secondary=\"true\"]:disabled {\n"
"    background: #f1f3f5;\n"
"    color: #9ca3af;\n"
"    border: 1px solid #e5e7eb;\n"
"}\n"
"\n"
"QPushButton#btnSearch {\n"
"    background: #0d6efd;\n"
"    color: #ffffff;\n"
"    border: 1px solid #0d6efd;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"}\n"
"QPushButton#btnSearch:hover {\n"
"    background: #0b5ed7;\n"
"    border-color: #0b5ed7;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    min-width: 72px;\n"
"}\n"
"QDialogButtonBox QPushButton {\n"
"    min-width: 84px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {\n"
"    background: #ffffff;\n"
"    border: 1px solid #d5dbe3;\n"
"    border-radius: 8px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: #2d66e4;\n"
"    selection-col"
                        "or: #ffffff;\n"
"}\n"
"QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid #2d66e4;\n"
"    background: #ffffff;\n"
"}\n"
"QLineEdit:disabled, QComboBox:disabled,\n"
"QSpinBox:disabled, QDoubleSpinBox:disabled {\n"
"    background: #f8f8f8;\n"
"    color: #abadae;\n"
"    border: 1px solid #e5e7eb;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #eef0f3;\n"
"    width: 22px;\n"
"}\n"
"\n"
"QMenu {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    padding: 4px;\n"
"}\n"
"QMenu::item {\n"
"    padding: 5px 18px;\n"
"    border-radius: 6px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background: #f5f7f9;\n"
"    color: #2d66e4;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 8px;\n"
"    outline: none;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 4px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background: #e8effc;\n"
"    color:"
                        " #111827;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #e5e7eb;\n"
"    background: #ffffff;\n"
"    border-radius: 8px;\n"
"    top: -1px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #f8f8f8;\n"
"    color: #6b7280;\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-bottom: none;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #2d66e4;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"}\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #d5dbe3;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #a"
                        "badae;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    height: 0;\n"
"    width: 0;\n"
"}\n"
"")
        self.centralwidget = QWidget(Stock_It)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QWidget(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.sideBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 24, 0, 0)
        self.titleContainer = QFrame(self.sideBar)
        self.titleContainer.setObjectName(u"titleContainer")
        self.titleContainer.setAutoFillBackground(False)
        self.titleContainer.setStyleSheet(u"background-color : transparent ; color:#ffffff ; font-weight : bold;\n"
"\n"
"border: none;")
        self.titleContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.titleContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, -1, -1, -1)
        self.title = QLabel(self.titleContainer)
        self.title.setObjectName(u"title")

        self.verticalLayout_2.addWidget(self.title, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.titleContainer, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sideBarConatainer = QFrame(self.sideBar)
        self.sideBarConatainer.setObjectName(u"sideBarConatainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBarConatainer.sizePolicy().hasHeightForWidth())
        self.sideBarConatainer.setSizePolicy(sizePolicy)
        self.sideBarConatainer.setStyleSheet(u"*{\n"
"background-color : #2563eb ; color:#ffffff;\n"
"\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgba(255,255,255,0.15) ; color:#ffffff\n"
"}\n"
"")
        self.sideBarConatainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.sideBarConatainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sideBarConatainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboardBtn = QPushButton(self.sideBarConatainer)
        self.dashboardBtn.setObjectName(u"dashboardBtn")

        self.verticalLayout.addWidget(self.dashboardBtn)

        self.stockBtn = QPushButton(self.sideBarConatainer)
        self.stockBtn.setObjectName(u"stockBtn")
        self.stockBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.stockBtn)

        self.entryBtn = QPushButton(self.sideBarConatainer)
        self.entryBtn.setObjectName(u"entryBtn")

        self.verticalLayout.addWidget(self.entryBtn)

        self.sortieBtn = QPushButton(self.sideBarConatainer)
        self.sortieBtn.setObjectName(u"sortieBtn")

        self.verticalLayout.addWidget(self.sortieBtn)

        self.mouvementBtn = QPushButton(self.sideBarConatainer)
        self.mouvementBtn.setObjectName(u"mouvementBtn")

        self.verticalLayout.addWidget(self.mouvementBtn)

        self.gestionBtn = QPushButton(self.sideBarConatainer)
        self.gestionBtn.setObjectName(u"gestionBtn")

        self.verticalLayout.addWidget(self.gestionBtn)


        self.verticalLayout_3.addWidget(self.sideBarConatainer, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.sideBar)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"*{\n"
"color:#ffffff;\n"
"\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgba(255,255,255,0.15) ; color:#ffffff\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.exitBtn = QPushButton(self.frame_3)
        self.exitBtn.setObjectName(u"exitBtn")

        self.verticalLayout_4.addWidget(self.exitBtn)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.sideBar)

        self.mainSection = QWidget(self.centralwidget)
        self.mainSection.setObjectName(u"mainSection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainSection.sizePolicy().hasHeightForWidth())
        self.mainSection.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.mainSection)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.mainSection)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainSection)

        Stock_It.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stock_It)
        self.exitBtn.clicked.connect(Stock_It.close)

        QMetaObject.connectSlotsByName(Stock_It)

    def retranslateUi(self, Stock_It):
        Stock_It.setWindowTitle(QCoreApplication.translate("StockIt", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("StockIt", u"Stock IT", None))
        self.dashboardBtn.setText(QCoreApplication.translate("StockIt", u"Tableau de bord", None))
        self.stockBtn.setText(QCoreApplication.translate("StockIt", u"Etat de stock", None))
        self.entryBtn.setText(QCoreApplication.translate("StockIt", u"Bon d'entr\u00e9e", None))
        self.sortieBtn.setText(QCoreApplication.translate("StockIt", u"Bon de sortie", None))
        self.mouvementBtn.setText(QCoreApplication.translate("StockIt", u"Mouvements d'un produit", None))
        self.gestionBtn.setText(QCoreApplication.translate("StockIt", u"Gestion des stock", None))
        self.exitBtn.setText(QCoreApplication.translate("StockIt", u"Quitter", None))

