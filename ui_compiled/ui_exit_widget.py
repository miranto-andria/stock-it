# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exit_widget.ui'
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

class Ui_exitWidget(object):
    def setupUi(self, exitWidget):
        if not exitWidget.objectName():
            exitWidget.setObjectName(u"exitWidget")
        exitWidget.resize(696, 506)
        exitWidget.setStyleSheet(u"\n"
"#middle{\n"
"border-radius : 8px;\n"
"border : 1px solid rgba(171, 173, 174, 40%); \n"
"background-color : #fff;\n"
"}\n"
"#description{\n"
"color : #abadae\n"
"}\n"
"\n"
"#searchBar{\n"
"background-color : #fff;\n"
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
        self.verticalLayout = QVBoxLayout(exitWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar = QWidget(exitWidget)
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
"color : white")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.horizontalLayout.addWidget(self.add)


        self.verticalLayout.addWidget(self.searchBar)

        self.middle = QWidget(exitWidget)
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

        self.exitTable = QTableWidget(self.middle)
        if (self.exitTable.columnCount() < 5):
            self.exitTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.exitTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.exitTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.exitTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.exitTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.exitTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.exitTable.setObjectName(u"exitTable")
        self.exitTable.setStyleSheet(u"")
        self.exitTable.setAlternatingRowColors(True)
        self.exitTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.exitTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.exitTable)


        self.verticalLayout.addWidget(self.middle)


        self.retranslateUi(exitWidget)

        QMetaObject.connectSlotsByName(exitWidget)
    # setupUi

    def retranslateUi(self, exitWidget):
        exitWidget.setWindowTitle(QCoreApplication.translate("exitWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("exitWidget", u"Bon de Sortie", None))
        self.description.setText(QCoreApplication.translate("exitWidget", u"G\u00e9rez les sorties de stock et suivez les approvisionnements en \u00e9quipements informatiques", None))
        self.btnAdd.setText(QCoreApplication.translate("exitWidget", u"Ajouter un bon", None))
        self.label_2.setText(QCoreApplication.translate("exitWidget", u"Filtrer par :", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("exitWidget", u"Num\u00e9ro du bon ,  produit ou par designation", None))
        self.btnSearch.setText(QCoreApplication.translate("exitWidget", u"Recherche", None))
        self.btnEdit.setText(QCoreApplication.translate("exitWidget", u"Modifier", None))
        self.btnDelete.setText(QCoreApplication.translate("exitWidget", u"Supprimer", None))
        ___qtablewidgetitem = self.exitTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("exitWidget", u"N\u00b0BON", None))
        ___qtablewidgetitem1 = self.exitTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("exitWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem2 = self.exitTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("exitWidget", u"Nom du Produit", None))
        ___qtablewidgetitem3 = self.exitTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("exitWidget", u"Quantite Sortie", None))
        ___qtablewidgetitem4 = self.exitTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("exitWidget", u"Date", None))
    # retranslateUi

