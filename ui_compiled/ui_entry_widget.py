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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_entryWidget(object):
    def setupUi(self, entryWidget):
        if not entryWidget.objectName():
            entryWidget.setObjectName(u"entryWidget")
        entryWidget.resize(576, 475)
        entryWidget.setStyleSheet(u"*{\n"
"background : #05060F;\n"
"}\n"
"#searchBar{\n"
"background : #13141F;\n"
"border-radius : 8px;\n"
"\n"
"}\n"
" #pageName , #search {\n"
"font-weight : bold;\n"
"background : transparent\n"
"}\n"
"\n"
"#searchInput{\n"
"background : transparent;\n"
"border: 1px solid #05060f;\n"
"border-radius : 8px;\n"
"width : 200px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(entryWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar = QWidget(entryWidget)
        self.searchBar.setObjectName(u"searchBar")
        self.horizontalLayout = QHBoxLayout(self.searchBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.pageName = QLabel(self.searchBar)
        self.pageName.setObjectName(u"pageName")
        self.pageName.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pageName)

        self.searchChoice = QComboBox(self.searchBar)
        self.searchChoice.setObjectName(u"searchChoice")

        self.horizontalLayout.addWidget(self.searchChoice)

        self.search = QFrame(self.searchBar)
        self.search.setObjectName(u"search")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setStyleSheet(u"")
        self.search.setFrameShape(QFrame.Shape.StyledPanel)
        self.search.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchInput = QLineEdit(self.search)
        self.searchInput.setObjectName(u"searchInput")

        self.horizontalLayout_2.addWidget(self.searchInput)

        self.btnSearch = QPushButton(self.search)
        self.btnSearch.setObjectName(u"btnSearch")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btnSearch.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnSearch)


        self.horizontalLayout.addWidget(self.search, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.searchBar, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(entryWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableTitle = QLabel(self.widget_2)
        self.tableTitle.setObjectName(u"tableTitle")

        self.horizontalLayout_3.addWidget(self.tableTitle)

        self.btnAjouter = QPushButton(self.widget_2)
        self.btnAjouter.setObjectName(u"btnAjouter")

        self.horizontalLayout_3.addWidget(self.btnAjouter)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(entryWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalLayout_2.addWidget(self.entryTable)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(entryWidget)

        QMetaObject.connectSlotsByName(entryWidget)
    # setupUi

    def retranslateUi(self, entryWidget):
        entryWidget.setWindowTitle(QCoreApplication.translate("entryWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("entryWidget", u"Bon d'entr\u00e9e", None))
        self.btnSearch.setText("")
        self.tableTitle.setText(QCoreApplication.translate("entryWidget", u"Liste des bon d'entr\u00e9e", None))
        self.btnAjouter.setText(QCoreApplication.translate("entryWidget", u"Ajouter", None))
        ___qtablewidgetitem = self.entryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("entryWidget", u"N\u00b0BON", None))
        ___qtablewidgetitem1 = self.entryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("entryWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem2 = self.entryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("entryWidget", u"Quantite Entr\u00e9e", None))
        ___qtablewidgetitem3 = self.entryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("entryWidget", u"Date", None))
    # retranslateUi

