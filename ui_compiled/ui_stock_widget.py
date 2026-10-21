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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_stockWidget(object):
    def setupUi(self, stockWidget):
        if not stockWidget.objectName():
            stockWidget.setObjectName(u"stockWidget")
        stockWidget.resize(874, 808)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        stockWidget.setFont(font)
        stockWidget.setStyleSheet(u"#stockWidget {\n"
"    font-family: \"Montserrat\";\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(stockWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.middle = QWidget(stockWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMinimumSize(QSize(0, 300))
        self.verticalLayout_11 = QVBoxLayout(self.middle)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.top = QWidget(self.middle)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 40))
        self.top.setStyleSheet(u"QLabel#textTotalProduct , QLabel#textTotalBondeSortie , QLabel#textTotalBondeEntree, QLabel#textTotalStock{\n"
"background-color: #ffffff;\n"
"color: #111827; border: 1px solid #e5e7eb;\n"
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
"background-color: #ffffff;\n"
"border : 1px solid #e5e7eb;\n"
"border-radius:8px;\n"
"padding: 10px;\n"
"}")
        self.cardHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.cardHeader)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalSpacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.horizontalLayout_13.addItem(self.verticalSpacer)

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


        self.verticalLayout_11.addWidget(self.top)

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
        self.table.setStyleSheet(u"")
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.table)


        self.gridLayout.addWidget(self.middle, 1, 0, 1, 1)

        self.bottom = QWidget(stockWidget)
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


        self.retranslateUi(stockWidget)

        QMetaObject.connectSlotsByName(stockWidget)
    # setupUi

    def retranslateUi(self, stockWidget):
        stockWidget.setWindowTitle(QCoreApplication.translate("stockWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("stockWidget", u"\u00c9tat de stock des produits", None))
        self.labelFilter.setText(QCoreApplication.translate("stockWidget", u"Filtre :", None))
        self.search.setPlaceholderText(QCoreApplication.translate("stockWidget", u"Filtrer par code ou d\u00e9signation\u2026", None))
        self.btnSearch.setText(QCoreApplication.translate("stockWidget", u"Recherche", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stockWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stockWidget", u"D\u00e9signation", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stockWidget", u"Stock", None))
        self.btnPdf.setText(QCoreApplication.translate("stockWidget", u"G\u00e9n\u00e9rer le PDF", None))
    # retranslateUi

