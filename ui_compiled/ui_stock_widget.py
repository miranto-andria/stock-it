# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from views.graphics import (HistogramWidget, PieChartWidget)

class Ui_stockWidget(object):
    def setupUi(self, stockWidget):
        if not stockWidget.objectName():
            stockWidget.setObjectName(u"stockWidget")
        stockWidget.resize(659, 808)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        stockWidget.setFont(font)
        stockWidget.setStyleSheet(u"* {\n"
"    font-family: \"Montserrat\";\n"
"    background-color: #f8f8f8;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(stockWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top = QWidget(stockWidget)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 195))
        self.top.setStyleSheet(u"QLabel#textTotalProduct , QLabel#textTotalBondeSortie , QLabel#textTotalBondeEntree, QLabel#textTotalStock{\n"
"background-color: #13141F;\n"
"color: white;\n"
"font:bold;\n"
"font-size: 22px;\n"
"qproperty-alignment: AlignCenter;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.top)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cardHeader = QFrame(self.top)
        self.cardHeader.setObjectName(u"cardHeader")
        self.cardHeader.setStyleSheet(u"#cardHeader{\n"
"background-color: #fff;\n"
"border-radius:8px;\n"
"padding: 10px;\n"
"border : 1px solid rgba(171, 173, 174, 40%);\n"
"}")
        self.cardHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.cardHeader)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.cardHeader)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(17)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label{\n"
"background-color:transparent;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label)


        self.verticalLayout_12.addWidget(self.cardHeader, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cardStock = QWidget(self.top)
        self.cardStock.setObjectName(u"cardStock")
        self.cardStock.setMinimumSize(QSize(0, 104))
        self.cardStock.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_3 = QVBoxLayout(self.cardStock)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.cardStock)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2)

        self.textTotalStock = QLabel(self.cardStock)
        self.textTotalStock.setObjectName(u"textTotalStock")
        self.textTotalStock.setStyleSheet(u"background-color : #fff;border : 1px solid rgba(171, 173, 174, 40%);")
        self.textTotalStock.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.textTotalStock)


        self.horizontalLayout_12.addWidget(self.cardStock)

        self.cardProduct = QWidget(self.top)
        self.cardProduct.setObjectName(u"cardProduct")
        self.cardProduct.setMinimumSize(QSize(0, 104))
        self.cardProduct.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_8 = QVBoxLayout(self.cardProduct)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.totalProduct = QLabel(self.cardProduct)
        self.totalProduct.setObjectName(u"totalProduct")
        self.totalProduct.setFont(font2)

        self.verticalLayout_8.addWidget(self.totalProduct)

        self.textTotalProduct = QLabel(self.cardProduct)
        self.textTotalProduct.setObjectName(u"textTotalProduct")
        self.textTotalProduct.setStyleSheet(u"background-color : #fff;border : 1px solid rgba(171, 173, 174, 40%);")
        self.textTotalProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.textTotalProduct)


        self.horizontalLayout_12.addWidget(self.cardProduct)

        self.cardBondeEntree = QWidget(self.top)
        self.cardBondeEntree.setObjectName(u"cardBondeEntree")
        self.cardBondeEntree.setMinimumSize(QSize(0, 104))
        self.cardBondeEntree.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_9 = QVBoxLayout(self.cardBondeEntree)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.totalBondeEntree = QLabel(self.cardBondeEntree)
        self.totalBondeEntree.setObjectName(u"totalBondeEntree")
        self.totalBondeEntree.setFont(font2)

        self.verticalLayout_9.addWidget(self.totalBondeEntree)

        self.textTotalBondeEntree = QLabel(self.cardBondeEntree)
        self.textTotalBondeEntree.setObjectName(u"textTotalBondeEntree")
        self.textTotalBondeEntree.setStyleSheet(u"background-color : #fff;border : 1px solid rgba(171, 173, 174, 40%);")
        self.textTotalBondeEntree.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.textTotalBondeEntree)


        self.horizontalLayout_12.addWidget(self.cardBondeEntree)

        self.cardBondeSortie = QWidget(self.top)
        self.cardBondeSortie.setObjectName(u"cardBondeSortie")
        self.cardBondeSortie.setMinimumSize(QSize(0, 104))
        self.cardBondeSortie.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_10 = QVBoxLayout(self.cardBondeSortie)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.totalBondeSortie = QLabel(self.cardBondeSortie)
        self.totalBondeSortie.setObjectName(u"totalBondeSortie")
        self.totalBondeSortie.setFont(font2)

        self.verticalLayout_10.addWidget(self.totalBondeSortie)

        self.textTotalBondeSortie = QLabel(self.cardBondeSortie)
        self.textTotalBondeSortie.setObjectName(u"textTotalBondeSortie")
        self.textTotalBondeSortie.setStyleSheet(u"background-color : #fff;border : 1px solid rgba(171, 173, 174, 40%);")
        self.textTotalBondeSortie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.textTotalBondeSortie)


        self.horizontalLayout_12.addWidget(self.cardBondeSortie)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addWidget(self.top)

        self.middle = QWidget(stockWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMinimumSize(QSize(0, 290))
        self.verticalLayout_11 = QVBoxLayout(self.middle)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setContentsMargins(-1, 8, 8, 8)
        self.labelFilter = QLabel(self.middle)
        self.labelFilter.setObjectName(u"labelFilter")

        self.searchLayout.addWidget(self.labelFilter)

        self.search = QLineEdit(self.middle)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 40))
        self.search.setStyleSheet(u"border : 1px solid rgba(171, 173, 174, 80%); background-color : #fff;")
        self.search.setClearButtonEnabled(True)

        self.searchLayout.addWidget(self.search)

        self.btnSearch = QPushButton(self.middle)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(0, 40))

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
        self.table.setMinimumSize(QSize(0, 210))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(10)
        self.table.setFont(font3)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.table)


        self.verticalLayout.addWidget(self.middle)

        self.bottom = QWidget(stockWidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 293))
        self.verticalLayout_2 = QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.bottom)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 200))
        self.histogrammeTab = QWidget()
        self.histogrammeTab.setObjectName(u"histogrammeTab")
        self.verticalLayout_13 = QVBoxLayout(self.histogrammeTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.histogramme = HistogramWidget(self.histogrammeTab)
        self.histogramme.setObjectName(u"histogramme")
        sizePolicy.setHeightForWidth(self.histogramme.sizePolicy().hasHeightForWidth())
        self.histogramme.setSizePolicy(sizePolicy)
        self.histogramme.setFrameShape(QFrame.Shape.StyledPanel)
        self.histogramme.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_13.addWidget(self.histogramme)

        self.tabWidget.addTab(self.histogrammeTab, "")
        self.camembertTab = QWidget()
        self.camembertTab.setObjectName(u"camembertTab")
        self.verticalLayout_14 = QVBoxLayout(self.camembertTab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.camembert = PieChartWidget(self.camembertTab)
        self.camembert.setObjectName(u"camembert")
        sizePolicy.setHeightForWidth(self.camembert.sizePolicy().hasHeightForWidth())
        self.camembert.setSizePolicy(sizePolicy)
        self.camembert.setFrameShape(QFrame.Shape.StyledPanel)
        self.camembert.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.camembert)

        self.tabWidget.addTab(self.camembertTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

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


        self.verticalLayout.addWidget(self.bottom)


        self.retranslateUi(stockWidget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(stockWidget)
    # setupUi

    def retranslateUi(self, stockWidget):
        stockWidget.setWindowTitle(QCoreApplication.translate("stockWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("stockWidget", u"\u00c9tat de stock des produits", None))
        self.label_2.setText(QCoreApplication.translate("stockWidget", u"Total Stock", None))
        self.textTotalStock.setText("")
        self.totalProduct.setText(QCoreApplication.translate("stockWidget", u"Produits", None))
        self.textTotalProduct.setText("")
        self.totalBondeEntree.setText(QCoreApplication.translate("stockWidget", u"Bons d'entr\u00e9e", None))
        self.textTotalBondeEntree.setText("")
        self.totalBondeSortie.setText(QCoreApplication.translate("stockWidget", u"Bons de sortie", None))
        self.textTotalBondeSortie.setText("")
        self.labelFilter.setText(QCoreApplication.translate("stockWidget", u"Filtre :", None))
        self.search.setPlaceholderText(QCoreApplication.translate("stockWidget", u"Filtrer par code ou d\u00e9signation\u2026", None))
        self.btnSearch.setText(QCoreApplication.translate("stockWidget", u"Recherche", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stockWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stockWidget", u"D\u00e9signation", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stockWidget", u"Stock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogrammeTab), QCoreApplication.translate("stockWidget", u"Histogramme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camembertTab), QCoreApplication.translate("stockWidget", u"Camembert", None))
        self.btnPdf.setText(QCoreApplication.translate("stockWidget", u"G\u00e9n\u00e9rer le PDF", None))
    # retranslateUi

