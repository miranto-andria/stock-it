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
        entryWidget.resize(783, 532)
        entryWidget.setStyleSheet(u"*{\n"
"background : #05060F;\n"
"}\n"
"#middle{\n"
"border-radius : 8px\n"
"}\n"
"\n"
"#searchBar{\n"
"background : #13141F;\n"
"border-radius : 8px;\n"
"padding : 50px\n"
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
"\n"
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
"QTableWidget"
                        "::item:selected {\n"
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
"QScrollBar::add-page:"
                        "vertical,\n"
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
"    border-radius: 4px;\n"
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

        self.searchChoice = QComboBox(self.searchBar)
        self.searchChoice.setObjectName(u"searchChoice")

        self.horizontalLayout.addWidget(self.searchChoice)

        self.search = QFrame(self.searchBar)
        self.search.setObjectName(u"search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy2)
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


        self.verticalLayout.addWidget(self.searchBar)

        self.middle = QWidget(entryWidget)
        self.middle.setObjectName(u"middle")
        sizePolicy.setHeightForWidth(self.middle.sizePolicy().hasHeightForWidth())
        self.middle.setSizePolicy(sizePolicy)
        self.middle.setStyleSheet(u"background : #13141F;\n"
"border : none")
        self.horizontalLayout_3 = QHBoxLayout(self.middle)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.entrContainer = QFrame(self.middle)
        self.entrContainer.setObjectName(u"entrContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.entrContainer.sizePolicy().hasHeightForWidth())
        self.entrContainer.setSizePolicy(sizePolicy3)
        self.entrContainer.setStyleSheet(u"")
        self.entrContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.entrContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.entrContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.label = QLabel(self.entrContainer)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"opacity : 0")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.entryCount = QLabel(self.entrContainer)
        self.entryCount.setObjectName(u"entryCount")
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.entryCount.setFont(font2)
        self.entryCount.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.entryCount, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_3.addWidget(self.entrContainer, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.middle)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.totalProduct = QLabel(self.frame_2)
        self.totalProduct.setObjectName(u"totalProduct")
        self.totalProduct.setFont(font)
        self.totalProduct.setStyleSheet(u"padding-right : 4px")
        self.totalProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.totalProduct, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_3.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.middle, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

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
        self.entryTable.setStyleSheet(u"")
        self.entryTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.entryTable)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(entryWidget)

        QMetaObject.connectSlotsByName(entryWidget)
    # setupUi

    def retranslateUi(self, entryWidget):
        entryWidget.setWindowTitle(QCoreApplication.translate("entryWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("entryWidget", u"Bon d'entr\u00e9e", None))
        self.btnSearch.setText("")
        self.label.setText(QCoreApplication.translate("entryWidget", u"Total de bon", None))
        self.entryCount.setText("")
        self.totalProduct.setText("")
        self.label_3.setText(QCoreApplication.translate("entryWidget", u"produits", None))
        ___qtablewidgetitem = self.entryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("entryWidget", u"N\u00b0BON", None))
        ___qtablewidgetitem1 = self.entryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("entryWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem2 = self.entryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("entryWidget", u"Quantite Entr\u00e9e", None))
        ___qtablewidgetitem3 = self.entryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("entryWidget", u"Date", None))
    # retranslateUi

