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
    QLabel, QLayout, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_stockWidget(object):
    def setupUi(self, stockWidget):
        if not stockWidget.objectName():
            stockWidget.setObjectName(u"stockWidget")
        stockWidget.resize(790, 700)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        stockWidget.setFont(font)
        stockWidget.setStyleSheet(u"* {\n"
"    font-family: \"Montserrat\";\n"
"    background-color: #05060f;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #13141F;\n"
"    alternate-background-color: #0D0E19;\n"
"    color: #f8f8ff;\n"
"\n"
"    border: 1px solid rgba(255, 255, 255, 20%);\n"
"    border-radius: 10px;\n"
"\n"
"    gridline-color: rgba(255, 255, 255, 8%);\n"
"    selection-background-color: #6243FF;\n"
"    selection-color: #f8f8ff;\n"
"\n"
"    outline: none;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px 8px;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(98, 67, 255, 18%);\n"
"    color: #f8f8ff;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #6243FF;\n"
"    color: #f8f8ff;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: #05060f;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #05060f;\n"
"    color: #f8f8ff;\n"
"\n"
"    padding: 12px 10px;\n"
"    border: none;\n"
""
                        "    border-bottom: 1px solid rgba(255, 255, 255, 15%);\n"
"\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #05060f;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #13141F;\n"
"    width: 8px;\n"
"    margin: 4px 2px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #3A3655;\n"
"    border-radius: 4px;\n"
"    min-height: 28px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #6243FF;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #13141F;\n"
"    height: 8px;\n"
"    margin: 2px 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3A3655;\n"
"    border-r"
                        "adius: 4px;\n"
"    min-width: 28px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #6243FF;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(stockWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top = QWidget(stockWidget)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 200))
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
"background-color: #13141F;\n"
"border-radius:8px;\n"
"padding: 10px;\n"
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
        self.horizontalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.cardStock = QWidget(self.top)
        self.cardStock.setObjectName(u"cardStock")
        self.cardStock.setMinimumSize(QSize(0, 140))
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
        self.textTotalStock.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.textTotalStock)


        self.horizontalLayout_12.addWidget(self.cardStock)

        self.cardProduct = QWidget(self.top)
        self.cardProduct.setObjectName(u"cardProduct")
        self.cardProduct.setMinimumSize(QSize(0, 140))
        self.cardProduct.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_8 = QVBoxLayout(self.cardProduct)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.totalProduct = QLabel(self.cardProduct)
        self.totalProduct.setObjectName(u"totalProduct")
        self.totalProduct.setFont(font2)

        self.verticalLayout_8.addWidget(self.totalProduct)

        self.textTotalProduct = QLabel(self.cardProduct)
        self.textTotalProduct.setObjectName(u"textTotalProduct")
        self.textTotalProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.textTotalProduct)


        self.horizontalLayout_12.addWidget(self.cardProduct)

        self.cardBondeEntree = QWidget(self.top)
        self.cardBondeEntree.setObjectName(u"cardBondeEntree")
        self.cardBondeEntree.setMinimumSize(QSize(0, 140))
        self.cardBondeEntree.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_9 = QVBoxLayout(self.cardBondeEntree)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.totalBondeEntree = QLabel(self.cardBondeEntree)
        self.totalBondeEntree.setObjectName(u"totalBondeEntree")
        self.totalBondeEntree.setFont(font2)

        self.verticalLayout_9.addWidget(self.totalBondeEntree)

        self.textTotalBondeEntree = QLabel(self.cardBondeEntree)
        self.textTotalBondeEntree.setObjectName(u"textTotalBondeEntree")
        self.textTotalBondeEntree.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.textTotalBondeEntree)


        self.horizontalLayout_12.addWidget(self.cardBondeEntree)

        self.cardBondeSortie = QWidget(self.top)
        self.cardBondeSortie.setObjectName(u"cardBondeSortie")
        self.cardBondeSortie.setMinimumSize(QSize(0, 140))
        self.cardBondeSortie.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_10 = QVBoxLayout(self.cardBondeSortie)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.totalBondeSortie = QLabel(self.cardBondeSortie)
        self.totalBondeSortie.setObjectName(u"totalBondeSortie")
        self.totalBondeSortie.setFont(font2)

        self.verticalLayout_10.addWidget(self.totalBondeSortie)

        self.textTotalBondeSortie = QLabel(self.cardBondeSortie)
        self.textTotalBondeSortie.setObjectName(u"textTotalBondeSortie")
        self.textTotalBondeSortie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.textTotalBondeSortie)


        self.horizontalLayout_12.addWidget(self.cardBondeSortie)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addWidget(self.top)

        self.middle = QWidget(stockWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMinimumSize(QSize(0, 340))
        self.verticalLayout_11 = QVBoxLayout(self.middle)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(10)
        self.table.setFont(font3)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.table)


        self.verticalLayout.addWidget(self.middle, 0, Qt.AlignmentFlag.AlignVCenter)

        self.bottom = QWidget(stockWidget)
        self.bottom.setObjectName(u"bottom")
        self.tabWidget = QTabWidget(self.bottom)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 29, 821, 181))
        self.histogramme = QWidget()
        self.histogramme.setObjectName(u"histogramme")
        self.tabWidget.addTab(self.histogramme, "")
        self.camembert = QWidget()
        self.camembert.setObjectName(u"camembert")
        self.tabWidget.addTab(self.camembert, "")

        self.verticalLayout.addWidget(self.bottom)


        self.retranslateUi(stockWidget)

        self.tabWidget.setCurrentIndex(0)


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
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stockWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stockWidget", u"D\u00e9signation", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stockWidget", u"Stock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogramme), QCoreApplication.translate("stockWidget", u"Histogramme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camembert), QCoreApplication.translate("stockWidget", u"Camembert", None))
    # retranslateUi

