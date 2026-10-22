# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movement_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MovementWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(811, 635)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.resume = QLabel(Form)
        self.resume.setObjectName(u"resume")
        self.resume.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.resume, 5, 0, 1, 1)

        self.table = QTableWidget(Form)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSortingEnabled(False)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout.addWidget(self.table, 4, 0, 1, 1)

        self.haut = QHBoxLayout()
        self.haut.setObjectName(u"haut")
        self.cadre_produit = QGroupBox(Form)
        self.cadre_produit.setObjectName(u"cadre_produit")
        self.ligne_produit = QHBoxLayout(self.cadre_produit)
        self.ligne_produit.setObjectName(u"ligne_produit")
        self.label_choix = QLabel(self.cadre_produit)
        self.label_choix.setObjectName(u"label_choix")

        self.ligne_produit.addWidget(self.label_choix)

        self.choix_produit = QComboBox(self.cadre_produit)
        self.choix_produit.setObjectName(u"choix_produit")
        self.choix_produit.setEditable(True)
        self.choix_produit.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.ligne_produit.addWidget(self.choix_produit)

        self.btn_rechercher = QPushButton(self.cadre_produit)
        self.btn_rechercher.setObjectName(u"btn_rechercher")
        self.btn_rechercher.setProperty(u"primaire", True)

        self.ligne_produit.addWidget(self.btn_rechercher)

        self.espace_produit = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ligne_produit.addItem(self.espace_produit)

        self.ligne_produit.setStretch(1, 1)
        self.ligne_produit.setStretch(3, 1)

        self.haut.addWidget(self.cadre_produit, 0, Qt.AlignmentFlag.AlignTop)

        self.cadre_periode = QGroupBox(Form)
        self.cadre_periode.setObjectName(u"cadre_periode")
        self.grille_periode = QGridLayout(self.cadre_periode)
        self.grille_periode.setObjectName(u"grille_periode")
        self.label_mode = QLabel(self.cadre_periode)
        self.label_mode.setObjectName(u"label_mode")

        self.grille_periode.addWidget(self.label_mode, 0, 0, 1, 1)

        self.mode = QComboBox(self.cadre_periode)
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.setObjectName(u"mode")

        self.grille_periode.addWidget(self.mode, 0, 1, 1, 1)

        self.periode = QLabel(self.cadre_periode)
        self.periode.setObjectName(u"periode")
        self.periode.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.grille_periode.addWidget(self.periode, 0, 3, 1, 1)

        self.label_du = QLabel(self.cadre_periode)
        self.label_du.setObjectName(u"label_du")

        self.grille_periode.addWidget(self.label_du, 1, 0, 1, 1)

        self.date_debut = QDateEdit(self.cadre_periode)
        self.date_debut.setObjectName(u"date_debut")
        self.date_debut.setCalendarPopup(True)

        self.grille_periode.addWidget(self.date_debut, 1, 1, 1, 1)

        self.label_au = QLabel(self.cadre_periode)
        self.label_au.setObjectName(u"label_au")

        self.grille_periode.addWidget(self.label_au, 1, 2, 1, 1)

        self.date_fin = QDateEdit(self.cadre_periode)
        self.date_fin.setObjectName(u"date_fin")
        self.date_fin.setCalendarPopup(True)

        self.grille_periode.addWidget(self.date_fin, 1, 3, 1, 1)

        self.label_mois = QLabel(self.cadre_periode)
        self.label_mois.setObjectName(u"label_mois")

        self.grille_periode.addWidget(self.label_mois, 2, 0, 1, 1)

        self.date_mois = QDateEdit(self.cadre_periode)
        self.date_mois.setObjectName(u"date_mois")
        self.date_mois.setCalendarPopup(True)

        self.grille_periode.addWidget(self.date_mois, 2, 1, 1, 1)

        self.label_annee = QLabel(self.cadre_periode)
        self.label_annee.setObjectName(u"label_annee")

        self.grille_periode.addWidget(self.label_annee, 3, 0, 1, 1)

        self.date_annee = QDateEdit(self.cadre_periode)
        self.date_annee.setObjectName(u"date_annee")
        self.date_annee.setCalendarPopup(True)

        self.grille_periode.addWidget(self.date_annee, 3, 1, 1, 1)

        self.espace_periode = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grille_periode.addItem(self.espace_periode, 0, 4, 4, 1)


        self.haut.addWidget(self.cadre_periode, 0, Qt.AlignmentFlag.AlignTop)

        self.haut.setStretch(0, 3)
        self.haut.setStretch(1, 2)

        self.gridLayout.addLayout(self.haut, 2, 0, 1, 1)

        self.sous_titre = QLabel(Form)
        self.sous_titre.setObjectName(u"sous_titre")

        self.gridLayout.addWidget(self.sous_titre, 1, 0, 1, 1)

        self.fiche = QGroupBox(Form)
        self.fiche.setObjectName(u"fiche")
        self.fiche_grille = QGridLayout(self.fiche)
        self.fiche_grille.setObjectName(u"fiche_grille")
        self.label_fiche_num = QLabel(self.fiche)
        self.label_fiche_num.setObjectName(u"label_fiche_num")

        self.fiche_grille.addWidget(self.label_fiche_num, 0, 0, 1, 1)

        self.lbl_num = QLabel(self.fiche)
        self.lbl_num.setObjectName(u"lbl_num")

        self.fiche_grille.addWidget(self.lbl_num, 0, 1, 1, 1)

        self.label_fiche_design = QLabel(self.fiche)
        self.label_fiche_design.setObjectName(u"label_fiche_design")

        self.fiche_grille.addWidget(self.label_fiche_design, 0, 2, 1, 1)

        self.lbl_design = QLabel(self.fiche)
        self.lbl_design.setObjectName(u"lbl_design")

        self.fiche_grille.addWidget(self.lbl_design, 0, 3, 1, 1)

        self.label_fiche_stock = QLabel(self.fiche)
        self.label_fiche_stock.setObjectName(u"label_fiche_stock")

        self.fiche_grille.addWidget(self.label_fiche_stock, 1, 0, 1, 1)

        self.lbl_stock = QLabel(self.fiche)
        self.lbl_stock.setObjectName(u"lbl_stock")

        self.fiche_grille.addWidget(self.lbl_stock, 1, 1, 1, 1)

        self.espace_fiche = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fiche_grille.addItem(self.espace_fiche, 0, 4, 2, 1)


        self.gridLayout.addWidget(self.fiche, 3, 0, 1, 1)

        self.titre = QLabel(Form)
        self.titre.setObjectName(u"titre")

        self.gridLayout.addWidget(self.titre, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("MovementWidget", u"Form", None))
        self.resume.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MovementWidget", u"N\u00b0 Bon", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MovementWidget", u"Entr\u00e9e", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MovementWidget", u"Sortie", None))
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MovementWidget", u"Date", None))
        self.cadre_produit.setTitle(QCoreApplication.translate("MovementWidget", u"Produit recherch\u00e9", None))
        self.label_choix.setText(QCoreApplication.translate("MovementWidget", u"N\u00b0 ou d\u00e9signation :", None))
        self.btn_rechercher.setText(QCoreApplication.translate("MovementWidget", u"Rechercher", None))
        self.cadre_periode.setTitle(QCoreApplication.translate("MovementWidget", u"P\u00e9riode de consultation", None))
        self.label_mode.setText(QCoreApplication.translate("MovementWidget", u"Mode :", None))
        self.mode.setItemText(0, QCoreApplication.translate("MovementWidget", u"Entre deux dates", None))
        self.mode.setItemText(1, QCoreApplication.translate("MovementWidget", u"Dans un mois", None))
        self.mode.setItemText(2, QCoreApplication.translate("MovementWidget", u"Dans une ann\u00e9e", None))
        self.mode.setItemText(3, QCoreApplication.translate("MovementWidget", u"Tout l'historique", None))

        self.periode.setText(QCoreApplication.translate("MovementWidget", u"P\u00e9riode : \u2014", None))
        self.label_du.setText(QCoreApplication.translate("MovementWidget", u"Du :", None))
        self.date_debut.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"dd/MM/yyyy", None))
        self.label_au.setText(QCoreApplication.translate("MovementWidget", u"Au :", None))
        self.date_fin.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"dd/MM/yyyy", None))
        self.label_mois.setText(QCoreApplication.translate("MovementWidget", u"Mois :", None))
        self.date_mois.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"MM/yyyy", None))
        self.label_annee.setText(QCoreApplication.translate("MovementWidget", u"Ann\u00e9e :", None))
        self.date_annee.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"yyyy", None))
        self.sous_titre.setText(QCoreApplication.translate("MovementWidget", u"S\u00e9lection par num\u00e9ro : N\u00b0 bon, quantit\u00e9 entr\u00e9e, quantit\u00e9 sortie et par date (entre 2 dates)", None))
        self.fiche.setTitle(QCoreApplication.translate("MovementWidget", u"Fiche produit", None))
        self.label_fiche_num.setText(QCoreApplication.translate("MovementWidget", u"N\u00b0 Produit :", None))
        self.lbl_num.setText(QCoreApplication.translate("MovementWidget", u"\u2014", None))
        self.label_fiche_design.setText(QCoreApplication.translate("MovementWidget", u"D\u00e9signation :", None))
        self.lbl_design.setText(QCoreApplication.translate("MovementWidget", u"\u2014", None))
        self.label_fiche_stock.setText(QCoreApplication.translate("MovementWidget", u"Stock actuel :", None))
        self.lbl_stock.setText(QCoreApplication.translate("MovementWidget", u"\u2014", None))
        self.titre.setText(QCoreApplication.translate("MovementWidget", u"Mouvements de stock d'un produit", None))
    # retranslateUi

