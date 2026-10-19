# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from views.graphics import (HistogramWidget, PieChartWidget)


class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(837, 636)
        dashboard.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(dashboard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(dashboard)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cardStock = QWidget(dashboard)
        self.cardStock.setObjectName(u"cardStock")
        self.cardStock.setMinimumSize(QSize(0, 104))
        self.cardStock.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_3 = QVBoxLayout(self.cardStock)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.cardStock)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u":/icons/product.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignLeft)

        self.textTotalStock = QLabel(self.cardStock)
        self.textTotalStock.setObjectName(u"textTotalStock")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.textTotalStock.setFont(font2)
        self.textTotalStock.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.textTotalStock)


        self.gridLayout.addWidget(self.cardStock, 0, 0, 1, 1)

        self.cardBondeEntree = QWidget(dashboard)
        self.cardBondeEntree.setObjectName(u"cardBondeEntree")
        self.cardBondeEntree.setMinimumSize(QSize(0, 104))
        self.cardBondeEntree.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_9 = QVBoxLayout(self.cardBondeEntree)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_2 = QPushButton(self.cardBondeEntree)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/inward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout_9.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.textTotalBondeEntree = QLabel(self.cardBondeEntree)
        self.textTotalBondeEntree.setObjectName(u"textTotalBondeEntree")
        self.textTotalBondeEntree.setFont(font2)
        self.textTotalBondeEntree.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.textTotalBondeEntree)


        self.gridLayout.addWidget(self.cardBondeEntree, 0, 2, 1, 1)

        self.cardProduct = QWidget(dashboard)
        self.cardProduct.setObjectName(u"cardProduct")
        self.cardProduct.setMinimumSize(QSize(0, 104))
        self.cardProduct.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_8 = QVBoxLayout(self.cardProduct)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.cardProduct)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/box.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.textTotalProduct = QLabel(self.cardProduct)
        self.textTotalProduct.setObjectName(u"textTotalProduct")
        self.textTotalProduct.setFont(font2)
        self.textTotalProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.textTotalProduct)


        self.gridLayout.addWidget(self.cardProduct, 0, 1, 1, 1)

        self.cardBondeSortie = QWidget(dashboard)
        self.cardBondeSortie.setObjectName(u"cardBondeSortie")
        self.cardBondeSortie.setMinimumSize(QSize(0, 104))
        self.cardBondeSortie.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalLayout_10 = QVBoxLayout(self.cardBondeSortie)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_3 = QPushButton(self.cardBondeSortie)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/outward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.textTotalBondeSortie = QLabel(self.cardBondeSortie)
        self.textTotalBondeSortie.setObjectName(u"textTotalBondeSortie")
        self.textTotalBondeSortie.setFont(font2)
        self.textTotalBondeSortie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.textTotalBondeSortie)


        self.gridLayout.addWidget(self.cardBondeSortie, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.histogramme = HistogramWidget(dashboard)
        self.histogramme.setObjectName(u"histogramme")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramme.sizePolicy().hasHeightForWidth())
        self.histogramme.setSizePolicy(sizePolicy)
        self.histogramme.setFrameShape(QFrame.Shape.StyledPanel)
        self.histogramme.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.histogramme)

        self.camembert = PieChartWidget(dashboard)
        self.camembert.setObjectName(u"camembert")
        sizePolicy.setHeightForWidth(self.camembert.sizePolicy().hasHeightForWidth())
        self.camembert.setSizePolicy(sizePolicy)
        self.camembert.setMinimumSize(QSize(0, 200))
        self.camembert.setFrameShape(QFrame.Shape.StyledPanel)
        self.camembert.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.camembert)


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"Tableau de bord des stocks", None))
        self.label_3.setText(QCoreApplication.translate("dashboard", u"Vue d'ensemble de la gestion de materiel informatique", None))
        self.pushButton_4.setText(QCoreApplication.translate("dashboard", u"Produits", None))
        self.textTotalStock.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("dashboard", u"Bons d'entr\u00e9es", None))
        self.textTotalBondeEntree.setText("")
        self.pushButton.setText(QCoreApplication.translate("dashboard", u"Stock total", None))
        self.textTotalProduct.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("dashboard", u"Bons de sortie", None))
        self.textTotalBondeSortie.setText("")
    # retranslateUi

