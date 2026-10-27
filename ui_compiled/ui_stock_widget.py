

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_StockWidget(object):
    def setupUi(self, StockWidget):
        if not StockWidget.objectName():
            StockWidget.setObjectName(u"StockWidget")
        StockWidget.resize(874, 808)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        StockWidget.setFont(font)
        StockWidget.setStyleSheet(u"#StockWidget { background: #f5f7f9; }\n"
"#StockWidget #cardHeader { background: #ffffff; border: 1px solid rgba(171,173,174,102); border-radius: 8px; }\n"
"#StockWidget #label { color: #111827; font-size: 18pt; font-weight: 700; background: transparent; }\n"
"#StockWidget #description { color: #abadae; font-size: 10pt; font-weight: 500; }\n"
"#StockWidget #btnSearch { background: #0d6efd; color: #ffffff; border: 1px solid #0d6efd; font-weight: 700; }\n"
"#StockWidget QTableWidget { alternate-background-color: #f3f6fb; selection-background-color: #dce8ff; }")
        self.gridLayout = QGridLayout(StockWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.middle = QWidget(StockWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMinimumSize(QSize(0, 300))
        self.verticalLayout_11 = QVBoxLayout(self.middle)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.searchBar = QWidget(self.middle)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(0, 40))
        self.verticalLayout_12 = QVBoxLayout(self.searchBar)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cardHeader = QFrame(self.searchBar)
        self.cardHeader.setObjectName(u"cardHeader")
        self.cardHeader.setStyleSheet(u"#cardHeader { background: #ffffff; border: 1px solid rgba(171,173,174,102); border-radius: 8px; padding: 12px;}")
        self.cardHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QVBoxLayout(self.cardHeader)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.cardHeader)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label{\n"
"background-color:transparent;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label)

        self.description = QLabel(self.cardHeader)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"color : #abadae")

        self.horizontalLayout_13.addWidget(self.description)


        self.verticalLayout_12.addWidget(self.cardHeader)


        self.verticalLayout_11.addWidget(self.searchBar)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setContentsMargins(-1, 8, 8, 8)
        self.labelFilter = QLabel(self.middle)
        self.labelFilter.setObjectName(u"labelFilter")

        self.searchLayout.addWidget(self.labelFilter)

        self.search = QLineEdit(self.middle)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 40))
        self.search.setClearButtonEnabled(True)

        self.searchLayout.addWidget(self.search)

        self.btnSearch = QPushButton(self.middle)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(0, 40))
        self.btnSearch.setStyleSheet(u"QPushButton { background-color : #0d6efd;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #0b5ed7; }\n"
"QPushButton:pressed { background-color : #0a58ca; }")
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QSize(17, 17))

        self.searchLayout.addWidget(self.btnSearch)

        self.searchLayout.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.searchLayout)

        self.table = QTableWidget(self.middle)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(0, 230))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(10)
        self.table.setFont(font2)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.table)


        self.gridLayout.addWidget(self.middle, 1, 0, 1, 1)

        self.bottom = QWidget(StockWidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 50))
        self.verticalLayout_2 = QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.barreActions = QHBoxLayout()
        self.barreActions.setObjectName(u"barreActions")
        self.espaceActions = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.barreActions.addItem(self.espaceActions)

        self.btnPdf = QPushButton(self.bottom)
        self.btnPdf.setObjectName(u"btnPdf")
        self.btnPdf.setMinimumSize(QSize(0, 40))
        self.btnPdf.setProperty(u"primaire", True)

        self.barreActions.addWidget(self.btnPdf)


        self.verticalLayout_2.addLayout(self.barreActions)


        self.gridLayout.addWidget(self.bottom, 2, 0, 1, 1)


        self.retranslateUi(StockWidget)

        QMetaObject.connectSlotsByName(StockWidget)

    def retranslateUi(self, StockWidget):
        StockWidget.setWindowTitle(QCoreApplication.translate("StockWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("StockWidget", u"\u00c9tat de stock des produits", None))
        self.description.setText(QCoreApplication.translate("StockWidget", u"Consultez les quantit\u00e9s disponibles et recherchez un produit par son code ou sa d\u00e9signation.", None))
        self.labelFilter.setText(QCoreApplication.translate("StockWidget", u"Filtre :", None))
        self.search.setPlaceholderText(QCoreApplication.translate("StockWidget", u"Filtrer par code ou d\u00e9signation\u2026", None))
        self.btnSearch.setText(QCoreApplication.translate("StockWidget", u"Recherche", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StockWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StockWidget", u"D\u00e9signation", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StockWidget", u"Stock", None))
        self.btnPdf.setText(QCoreApplication.translate("StockWidget", u"G\u00e9n\u00e9rer le PDF", None))

