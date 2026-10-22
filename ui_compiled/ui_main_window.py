# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Stock_It(object):
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
"background : #fff;\n"
"}\n"
"\n"
"#sideBar QPushButton{\n"
"text-align : left;\n"
"border : none;\n"
"margin : 2px 10px;\n"
"padding : 11px 14px;\n"
"border-radius : 8px;\n"
"font-size : 10.5pt;\n"
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
"#mainSection #stackedWidget{\n"
"background-color : #f5f7f9\n"
"} ")
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
    # setupUi

    def retranslateUi(self, Stock_It):
        Stock_It.setWindowTitle(QCoreApplication.translate("Stock_It", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Stock_It", u"Stock IT", None))
        self.dashboardBtn.setText(QCoreApplication.translate("Stock_It", u"Tableau de bord", None))
        self.stockBtn.setText(QCoreApplication.translate("Stock_It", u"Etat de stock", None))
        self.entryBtn.setText(QCoreApplication.translate("Stock_It", u"Bon d'entr\u00e9e", None))
        self.sortieBtn.setText(QCoreApplication.translate("Stock_It", u"Bon de sortie", None))
        self.mouvementBtn.setText(QCoreApplication.translate("Stock_It", u"Mouvements d'un produit", None))
        self.gestionBtn.setText(QCoreApplication.translate("Stock_It", u"Gestion des stock", None))
        self.exitBtn.setText(QCoreApplication.translate("Stock_It", u"Quitter", None))
    # retranslateUi

