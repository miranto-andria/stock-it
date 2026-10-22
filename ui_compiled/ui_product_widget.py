# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_productWidget(object):
    def setupUi(self, productWidget):
        if not productWidget.objectName():
            productWidget.setObjectName(u"productWidget")
        productWidget.resize(783, 532)
        productWidget.setStyleSheet(u"\n"
"#middle{\n"
"border-radius : 8px;\n"
"border : 1px solid rgba(171, 173, 174, 40%); \n"
"background-color : #fff;\n"
"}\n"
"#description{\n"
"color : #abadae\n"
"}\n"
"\n"
"\n"
"#searchBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius : 8px;\n"
"padding : 50px;\n"
"border : 1px solid rgba(171, 173, 174, 40%);\n"
"\n"
"}\n"
" #pageName , #add {\n"
"font-weight : bold;\n"
"background : transparent;\n"
"}\n"
"QPushButton , QComboBox{\n"
"padding : 8px 16px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(productWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar = QWidget(productWidget)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.searchBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.searchBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pageName = QLabel(self.frame_2)
        self.pageName.setObjectName(u"pageName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pageName.sizePolicy().hasHeightForWidth())
        self.pageName.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pageName.setFont(font)
        self.pageName.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pageName)

        self.description = QLabel(self.frame_2)
        self.description.setObjectName(u"description")

        self.verticalLayout_3.addWidget(self.description)


        self.horizontalLayout.addWidget(self.frame_2)

        self.add = QFrame(self.searchBar)
        self.add.setObjectName(u"add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy2)
        self.add.setStyleSheet(u"")
        self.add.setFrameShape(QFrame.Shape.StyledPanel)
        self.add.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.add)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(self.add)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"background-color : #774cff;\n"
"font : bold;\n"
"border : none;\n"
"color:  white")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.horizontalLayout.addWidget(self.add)


        self.verticalLayout.addWidget(self.searchBar)

        self.middle = QWidget(productWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.middle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.middle)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.searchInput = QLineEdit(self.frame)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setStyleSheet(u"padding : 8px 16px;\n"
"border : 1px solid rgba(171, 173, 174, 80%); background-color : #fff;")

        self.horizontalLayout_5.addWidget(self.searchInput)

        self.btnSearch = QPushButton(self.frame)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setStyleSheet(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btnSearch.setIcon(icon1)
        self.btnSearch.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnSearch)

        self.btnEdit = QPushButton(self.frame)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"border : 1px solid rgba(171, 173, 174, 40%);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setStyleSheet(u"background :#e74c3c;\n"
"border : none\n"
"")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnDelete)


        self.verticalLayout_2.addWidget(self.frame)

        self.productTable = QTableWidget(self.middle)
        if (self.productTable.columnCount() < 3):
            self.productTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.productTable.setObjectName(u"productTable")
        self.productTable.setStyleSheet(u"")
        self.productTable.setAlternatingRowColors(True)
        self.productTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.productTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.productTable)


        self.verticalLayout.addWidget(self.middle)


        self.retranslateUi(productWidget)

        QMetaObject.connectSlotsByName(productWidget)
    # setupUi

    def retranslateUi(self, productWidget):
        productWidget.setWindowTitle(QCoreApplication.translate("productWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("productWidget", u"Gestion et listage des profuits", None))
        self.description.setText(QCoreApplication.translate("productWidget", u"Consultez les \u00e9quipements disponibles et suivez les quantit\u00e9s en stock en temps r\u00e9el", None))
        self.btnAdd.setText(QCoreApplication.translate("productWidget", u"Ajouter un produit", None))
        self.label_2.setText(QCoreApplication.translate("productWidget", u"Filtrer par :", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("productWidget", u"Num\u00e9ro du produit ou designation", None))
        self.btnSearch.setText(QCoreApplication.translate("productWidget", u"Recherche", None))
        self.btnEdit.setText(QCoreApplication.translate("productWidget", u"Modifier", None))
        self.btnDelete.setText(QCoreApplication.translate("productWidget", u"Supprimer", None))
        ___qtablewidgetitem = self.productTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("productWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.productTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("productWidget", u"Designation", None))
        ___qtablewidgetitem2 = self.productTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("productWidget", u"Stock", None))
    # retranslateUi

