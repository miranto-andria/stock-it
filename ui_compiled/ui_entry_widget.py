# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entry_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_entryWidget(object):
    def setupUi(self, entryWidget):
        if not entryWidget.objectName():
            entryWidget.setObjectName(u"entryWidget")
        entryWidget.resize(783, 532)
        entryWidget.setStyleSheet(u"\n"
"#middle{\n"
"border-radius : 8px\n"
"}\n"
"\n"
"#searchBar{\n"
"background : #13141F;\n"
"border-radius : 8px;\n"
"padding : 50px\n"
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
        self.verticalLayout = QVBoxLayout(entryWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar = QWidget(entryWidget)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.searchBar)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 8, 16, 8)
        self.pageName = QLabel(self.searchBar)
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

        self.horizontalLayout.addWidget(self.pageName)

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
        self.btnAdd.setStyleSheet(u"background-color : #6243FF;\n"
"font : bold")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.horizontalLayout.addWidget(self.add)


        self.verticalLayout.addWidget(self.searchBar)

        self.widget_3 = QWidget(entryWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.searchChoice = QComboBox(self.frame)
        self.searchChoice.setObjectName(u"searchChoice")
        self.searchChoice.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.searchChoice)

        self.searchInput = QLineEdit(self.frame)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setStyleSheet(u"padding : 8px 16px")

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
        self.btnEdit.setStyleSheet(u"")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setStyleSheet(u"background :#e74c3c")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnDelete)


        self.verticalLayout_2.addWidget(self.frame)

        self.entryTable = QTableWidget(self.widget_3)
        if (self.entryTable.columnCount() < 4):
            self.entryTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.entryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.entryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.entryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.entryTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.entryTable.setObjectName(u"entryTable")
        self.entryTable.setStyleSheet(u"")
        self.entryTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.entryTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.entryTable)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(entryWidget)

        QMetaObject.connectSlotsByName(entryWidget)
    # setupUi

    def retranslateUi(self, entryWidget):
        entryWidget.setWindowTitle(QCoreApplication.translate("entryWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("entryWidget", u"Bon d'entr\u00e9e", None))
        self.btnAdd.setText(QCoreApplication.translate("entryWidget", u"Ajouter un bon", None))
        self.label_2.setText(QCoreApplication.translate("entryWidget", u"Filtrer par :", None))
        self.btnSearch.setText(QCoreApplication.translate("entryWidget", u"Recherche", None))
        self.btnEdit.setText(QCoreApplication.translate("entryWidget", u"Modifier", None))
        self.btnDelete.setText(QCoreApplication.translate("entryWidget", u"Supprimer", None))
        ___qtablewidgetitem = self.entryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("entryWidget", u"N\u00b0BON", None))
        ___qtablewidgetitem1 = self.entryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("entryWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem2 = self.entryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("entryWidget", u"Quantite Entr\u00e9e", None))
        ___qtablewidgetitem3 = self.entryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("entryWidget", u"Date", None))
    # retranslateUi

