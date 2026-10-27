

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MovementWidget(object):
    def setupUi(self, MovementWidget):
        if not MovementWidget.objectName():
            MovementWidget.setObjectName(u"MovementWidget")
        MovementWidget.resize(811, 676)
        MovementWidget.setStyleSheet(u"#MovementWidget { background: #f5f7f9; }\n"
"#MovementWidget #titre { color: #111827; font-size: 18pt; font-weight: 700; }\n"
"#MovementWidget #sous_titre { color: #6b7280; font-size: 9.5pt; }\n"
"#MovementWidget QGroupBox { background: #ffffff; border: 1px solid rgba(171,173,174,102); border-radius: 8px; margin-top: 14px; padding: 12px; }\n"
"#MovementWidget QGroupBox::title { color: #2d66e4; font-size: 10pt; font-weight: 700; }\n"
"#MovementWidget #fiche { border-left: 4px solid #2d66e4; }\n"
"#MovementWidget #label_fiche_num, #MovementWidget #label_fiche_design, #MovementWidget #label_fiche_stock, #MovementWidget #label_choix, #MovementWidget #label_mode, #MovementWidget #label_du, #MovementWidget #label_au, #MovementWidget #label_mois, #MovementWidget #label_annee { color: #6b7280; font-size: 9pt; font-weight: 600; }\n"
"#MovementWidget #lbl_num, #MovementWidget #lbl_design, #MovementWidget #lbl_stock { color: #111827; font-size: 11pt; font-weight: 700; }\n"
"#MovementWidget #lbl_stock { color: #2d66e4; fo"
                        "nt-size: 13pt; }\n"
"#MovementWidget #periode { color: #2d66e4; font-size: 9pt; font-weight: 700; }\n"
"#MovementWidget QDateEdit { background: #ffffff; border: 1px solid #d5dbe3; border-radius: 8px; padding: 6px 8px; }\n"
"#MovementWidget QDateEdit:focus { border-color: #2d66e4; }\n"
"#MovementWidget QDateEdit:disabled { background: #f8f8f8; color: #abadae; border-color: #e5e7eb; }\n"
"#MovementWidget QTableWidget { border-radius: 10px; font-size: 9.5pt; }\n"
"#MovementWidget QHeaderView::section { padding: 10px 8px; font-size: 9pt; }\n"
"#MovementWidget #resume { background: #ffffff; border: 1px solid #dfe7f7; border-radius: 10px; color: #374151; font-size: 10pt; font-weight: 600; padding: 11px 14px; }")
        self.gridLayout = QGridLayout(MovementWidget)
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.resume = QLabel(MovementWidget)
        self.resume.setObjectName(u"resume")
        self.resume.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.resume, 5, 0, 1, 1)

        self.tableCard = QFrame(MovementWidget)
        self.tableCard.setObjectName(u"tableCard")
        self.tableCard.setStyleSheet(u"#tableCard { background: #ffffff; border: 1px solid rgba(171,173,174,102); border-radius: 8px; padding: 8px; }")
        self.tableCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableCardLayout = QVBoxLayout(self.tableCard)
        self.tableCardLayout.setObjectName(u"tableCardLayout")
        self.table = QTableWidget(self.tableCard)
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

        self.tableCardLayout.addWidget(self.table)


        self.gridLayout.addWidget(self.tableCard, 4, 0, 1, 1)

        self.haut = QHBoxLayout()
        self.haut.setObjectName(u"haut")
        self.cadre_produit = QGroupBox(MovementWidget)
        self.cadre_produit.setObjectName(u"cadre_produit")
        self.ligne_produit = QHBoxLayout(self.cadre_produit)
        self.ligne_produit.setObjectName(u"ligne_produit")
        self.label_choix = QLabel(self.cadre_produit)
        self.label_choix.setObjectName(u"label_choix")

        self.ligne_produit.addWidget(self.label_choix)

        self.choix_produit = QLineEdit(self.cadre_produit)
        self.choix_produit.setObjectName(u"choix_produit")
        self.choix_produit.setClearButtonEnabled(True)

        self.ligne_produit.addWidget(self.choix_produit)

        self.btn_rechercher = QPushButton(self.cadre_produit)
        self.btn_rechercher.setObjectName(u"btn_rechercher")
        self.btn_rechercher.setStyleSheet(u"QPushButton { background-color : #0d6efd;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #0b5ed7; }\n"
"QPushButton:pressed { background-color : #0a58ca; }")
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rechercher.setIcon(icon)
        self.btn_rechercher.setProperty(u"primaire", True)

        self.ligne_produit.addWidget(self.btn_rechercher)

        self.ligne_produit.setStretch(1, 1)

        self.haut.addWidget(self.cadre_produit, 0, Qt.AlignmentFlag.AlignTop)

        self.cadre_periode = QGroupBox(MovementWidget)
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

        self.fiche = QGroupBox(MovementWidget)
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

        self.searchBar = QWidget(MovementWidget)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setStyleSheet(u"#searchBar{background: #ffffff; border: 1px solid rgba(171,173,174,102); border-radius: 8px; \n"
"padding: 15px;}")
        self.headerLayout = QVBoxLayout(self.searchBar)
        self.headerLayout.setSpacing(6)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(15, 15, 15, 15)
        self.titre = QLabel(self.searchBar)
        self.titre.setObjectName(u"titre")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titre.setFont(font)

        self.headerLayout.addWidget(self.titre)

        self.sous_titre = QLabel(self.searchBar)
        self.sous_titre.setObjectName(u"sous_titre")
        self.sous_titre.setStyleSheet(u"")

        self.headerLayout.addWidget(self.sous_titre)


        self.gridLayout.addWidget(self.searchBar, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)


        self.retranslateUi(MovementWidget)

        QMetaObject.connectSlotsByName(MovementWidget)

    def retranslateUi(self, MovementWidget):
        MovementWidget.setWindowTitle(QCoreApplication.translate("MovementWidget", u"Form", None))
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
        self.choix_produit.setPlaceholderText(QCoreApplication.translate("MovementWidget", u"Code ou d\u00e9signation du produit", None))
        self.btn_rechercher.setText(QCoreApplication.translate("MovementWidget", u"Rechercher", None))
        self.cadre_periode.setTitle(QCoreApplication.translate("MovementWidget", u"P\u00e9riode de consultation", None))
        self.label_mode.setText(QCoreApplication.translate("MovementWidget", u"Mode :", None))
        self.mode.setItemText(0, QCoreApplication.translate("MovementWidget", u"Entre deux dates", None))
        self.mode.setItemText(1, QCoreApplication.translate("MovementWidget", u"Dans un mois", None))
        self.mode.setItemText(2, QCoreApplication.translate("MovementWidget", u"Dans une ann\u00e9e", None))
        self.mode.setItemText(3, QCoreApplication.translate("MovementWidget", u"Tout l'historique", None))

        self.periode.setText(QCoreApplication.translate("MovementWidget", u"-", None))
        self.label_du.setText(QCoreApplication.translate("MovementWidget", u"Du :", None))
        self.date_debut.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"dd/MM/yyyy", None))
        self.label_au.setText(QCoreApplication.translate("MovementWidget", u"Au :", None))
        self.date_fin.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"dd/MM/yyyy", None))
        self.label_mois.setText(QCoreApplication.translate("MovementWidget", u"Mois :", None))
        self.date_mois.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"MM/yyyy", None))
        self.label_annee.setText(QCoreApplication.translate("MovementWidget", u"Ann\u00e9e :", None))
        self.date_annee.setDisplayFormat(QCoreApplication.translate("MovementWidget", u"yyyy", None))
        self.fiche.setTitle(QCoreApplication.translate("MovementWidget", u"Fiche produit", None))
        self.label_fiche_num.setText(QCoreApplication.translate("MovementWidget", u"N\u00b0 Produit :", None))
        self.lbl_num.setText(QCoreApplication.translate("MovementWidget", u"-", None))
        self.label_fiche_design.setText(QCoreApplication.translate("MovementWidget", u"D\u00e9signation :", None))
        self.lbl_design.setText(QCoreApplication.translate("MovementWidget", u"-", None))
        self.label_fiche_stock.setText(QCoreApplication.translate("MovementWidget", u"Stock actuel :", None))
        self.lbl_stock.setText(QCoreApplication.translate("MovementWidget", u"-", None))
        self.titre.setText(QCoreApplication.translate("MovementWidget", u"Mouvements de stock d'un produit", None))
        self.sous_titre.setText(QCoreApplication.translate("MovementWidget", u"Consultez les entr\u00e9es et sorties selon le produit et la p\u00e9riode s\u00e9lectionn\u00e9s.", None))

