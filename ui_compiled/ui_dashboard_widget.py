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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QVBoxLayout, QWidget)

from views.graphics import (HistogramWidget, PieChartWidget)
import resources_rc

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
        self.frame.setStyleSheet(u"padding: 2px 3px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.stats = QLabel(self.frame)
        self.stats.setObjectName(u"stats")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(8)
        font1.setKerning(False)
        self.stats.setFont(font1)

        self.verticalLayout.addWidget(self.stats)


        self.verticalLayout_2.addWidget(self.frame)

        self.grille = QGridLayout()
        self.grille.setSpacing(12)
        self.grille.setObjectName(u"grille")
        self.carte_produits = QWidget(dashboard)
        self.carte_produits.setObjectName(u"carte_produits")
        self.carte_produits.setStyleSheet(u"")
        self.layout_carte_produits = QHBoxLayout(self.carte_produits)
        self.layout_carte_produits.setSpacing(12)
        self.layout_carte_produits.setObjectName(u"layout_carte_produits")
        self.layout_carte_produits.setContentsMargins(14, 12, 14, 12)
        self.tile_ico_produits = QLabel(self.carte_produits)
        self.tile_ico_produits.setObjectName(u"tile_ico_produits")
        self.tile_ico_produits.setMinimumSize(QSize(40, 40))
        self.tile_ico_produits.setMaximumSize(QSize(40, 40))
        self.tile_ico_produits.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_carte_produits.addWidget(self.tile_ico_produits)

        self.colonne_produits = QVBoxLayout()
        self.colonne_produits.setSpacing(3)
        self.colonne_produits.setObjectName(u"colonne_produits")
        self.titre_produits = QLabel(self.carte_produits)
        self.titre_produits.setObjectName(u"titre_produits")

        self.colonne_produits.addWidget(self.titre_produits)

        self.valeur_produits = QLabel(self.carte_produits)
        self.valeur_produits.setObjectName(u"valeur_produits")

        self.colonne_produits.addWidget(self.valeur_produits)


        self.layout_carte_produits.addLayout(self.colonne_produits)


        self.grille.addWidget(self.carte_produits, 0, 0, 1, 1)

        self.carte_stock = QWidget(dashboard)
        self.carte_stock.setObjectName(u"carte_stock")
        self.layout_carte_stock = QHBoxLayout(self.carte_stock)
        self.layout_carte_stock.setSpacing(12)
        self.layout_carte_stock.setObjectName(u"layout_carte_stock")
        self.layout_carte_stock.setContentsMargins(14, 12, 14, 12)
        self.tile_ico_stock = QLabel(self.carte_stock)
        self.tile_ico_stock.setObjectName(u"tile_ico_stock")
        self.tile_ico_stock.setMinimumSize(QSize(40, 40))
        self.tile_ico_stock.setMaximumSize(QSize(40, 40))
        self.tile_ico_stock.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_carte_stock.addWidget(self.tile_ico_stock)

        self.colonne_stock = QVBoxLayout()
        self.colonne_stock.setSpacing(3)
        self.colonne_stock.setObjectName(u"colonne_stock")
        self.titre_stock = QLabel(self.carte_stock)
        self.titre_stock.setObjectName(u"titre_stock")

        self.colonne_stock.addWidget(self.titre_stock)

        self.valeur_stock = QLabel(self.carte_stock)
        self.valeur_stock.setObjectName(u"valeur_stock")

        self.colonne_stock.addWidget(self.valeur_stock)


        self.layout_carte_stock.addLayout(self.colonne_stock)


        self.grille.addWidget(self.carte_stock, 0, 1, 1, 1)

        self.carte_entrees = QWidget(dashboard)
        self.carte_entrees.setObjectName(u"carte_entrees")
        self.layout_carte_entrees = QHBoxLayout(self.carte_entrees)
        self.layout_carte_entrees.setSpacing(12)
        self.layout_carte_entrees.setObjectName(u"layout_carte_entrees")
        self.layout_carte_entrees.setContentsMargins(14, 12, 14, 12)
        self.tile_ico_entrees = QLabel(self.carte_entrees)
        self.tile_ico_entrees.setObjectName(u"tile_ico_entrees")
        self.tile_ico_entrees.setMinimumSize(QSize(40, 40))
        self.tile_ico_entrees.setMaximumSize(QSize(40, 40))
        self.tile_ico_entrees.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_carte_entrees.addWidget(self.tile_ico_entrees)

        self.colonne_entrees = QVBoxLayout()
        self.colonne_entrees.setSpacing(3)
        self.colonne_entrees.setObjectName(u"colonne_entrees")
        self.titre_entrees = QLabel(self.carte_entrees)
        self.titre_entrees.setObjectName(u"titre_entrees")

        self.colonne_entrees.addWidget(self.titre_entrees)

        self.valeur_entrees = QLabel(self.carte_entrees)
        self.valeur_entrees.setObjectName(u"valeur_entrees")

        self.colonne_entrees.addWidget(self.valeur_entrees)


        self.layout_carte_entrees.addLayout(self.colonne_entrees)


        self.grille.addWidget(self.carte_entrees, 0, 2, 1, 1)

        self.carte_sorties = QWidget(dashboard)
        self.carte_sorties.setObjectName(u"carte_sorties")
        self.layout_carte_sorties = QHBoxLayout(self.carte_sorties)
        self.layout_carte_sorties.setSpacing(12)
        self.layout_carte_sorties.setObjectName(u"layout_carte_sorties")
        self.layout_carte_sorties.setContentsMargins(14, 12, 14, 12)
        self.tile_ico_sorties = QLabel(self.carte_sorties)
        self.tile_ico_sorties.setObjectName(u"tile_ico_sorties")
        self.tile_ico_sorties.setMinimumSize(QSize(40, 40))
        self.tile_ico_sorties.setMaximumSize(QSize(40, 40))
        self.tile_ico_sorties.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_carte_sorties.addWidget(self.tile_ico_sorties)

        self.colonne_sorties = QVBoxLayout()
        self.colonne_sorties.setSpacing(3)
        self.colonne_sorties.setObjectName(u"colonne_sorties")
        self.colonne_sorties.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.titre_sorties = QLabel(self.carte_sorties)
        self.titre_sorties.setObjectName(u"titre_sorties")

        self.colonne_sorties.addWidget(self.titre_sorties)

        self.valeur_sorties = QLabel(self.carte_sorties)
        self.valeur_sorties.setObjectName(u"valeur_sorties")

        self.colonne_sorties.addWidget(self.valeur_sorties)

        self.colonne_sorties.setStretch(1, 3)

        self.layout_carte_sorties.addLayout(self.colonne_sorties)


        self.grille.addWidget(self.carte_sorties, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.grille)

        self.ligne_graphiques = QHBoxLayout()
        self.ligne_graphiques.setSpacing(12)
        self.ligne_graphiques.setObjectName(u"ligne_graphiques")
        self.cadre_histogramme = QWidget(dashboard)
        self.cadre_histogramme.setObjectName(u"cadre_histogramme")
        self.layout_cadre_histogramme = QVBoxLayout(self.cadre_histogramme)
        self.layout_cadre_histogramme.setObjectName(u"layout_cadre_histogramme")
        self.layout_cadre_histogramme.setContentsMargins(6, 6, 6, 6)
        self.histogramme = HistogramWidget(self.cadre_histogramme)
        self.histogramme.setObjectName(u"histogramme")

        self.layout_cadre_histogramme.addWidget(self.histogramme)


        self.ligne_graphiques.addWidget(self.cadre_histogramme)

        self.cadre_camembert = QWidget(dashboard)
        self.cadre_camembert.setObjectName(u"cadre_camembert")
        self.layout_cadre_camembert = QVBoxLayout(self.cadre_camembert)
        self.layout_cadre_camembert.setObjectName(u"layout_cadre_camembert")
        self.layout_cadre_camembert.setContentsMargins(6, 4, 6, 6)
        self.camembert = PieChartWidget(self.cadre_camembert)
        self.camembert.setObjectName(u"camembert")

        self.layout_cadre_camembert.addWidget(self.camembert)


        self.ligne_graphiques.addWidget(self.cadre_camembert)

        self.ligne_graphiques.setStretch(0, 1)
        self.ligne_graphiques.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.ligne_graphiques)

        self.bloc_mouvements = QGroupBox(dashboard)
        self.bloc_mouvements.setObjectName(u"bloc_mouvements")
        self.layout_mouvements = QVBoxLayout(self.bloc_mouvements)
        self.layout_mouvements.setObjectName(u"layout_mouvements")
        self.layout_mouvements.setContentsMargins(-1, -1, -1, 6)
        self.derniers_mouvements = QListWidget(self.bloc_mouvements)
        self.derniers_mouvements.setObjectName(u"derniers_mouvements")
        self.derniers_mouvements.setMinimumSize(QSize(0, 150))

        self.layout_mouvements.addWidget(self.derniers_mouvements)


        self.verticalLayout_2.addWidget(self.bloc_mouvements)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"Tableau de bord des stocks", None))
        self.stats.setText("")
        self.tile_ico_produits.setText("")
        self.titre_produits.setText(QCoreApplication.translate("dashboard", u"Nombre de produits", None))
        self.valeur_produits.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.tile_ico_stock.setText("")
        self.titre_stock.setText(QCoreApplication.translate("dashboard", u"Quantit\u00e9 totale en stock", None))
        self.valeur_stock.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.tile_ico_entrees.setText("")
        self.titre_entrees.setText(QCoreApplication.translate("dashboard", u"Bons d'entr\u00e9e", None))
        self.valeur_entrees.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.tile_ico_sorties.setText("")
        self.titre_sorties.setText(QCoreApplication.translate("dashboard", u"Bons de sortie", None))
        self.valeur_sorties.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.bloc_mouvements.setTitle(QCoreApplication.translate("dashboard", u"Derniers mouvements enregistr\u00e9s", None))
    # retranslateUi

