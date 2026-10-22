from calendar import monthrange
from datetime import date

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QInputDialog, QMessageBox, QWidget

import db
import utils.table_management as tbm
from ui_compiled.ui_movement_widget import Ui_MovementWidget

MODE_INTERVALLE = 0
MODE_MOIS = 1
MODE_ANNEE = 2
MODE_TOUT = 3


class MovementWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MovementWidget()
        self.ui.setupUi(self)

        self.produit_courant = None

        tbm.columns_setting(self.ui.table, [150, 120, 120, 0], colonne_etirable=3)
        self.ui.table.verticalHeader().setVisible(False)

        self.ui.date_debut.setDate(QDate.currentDate().addMonths(-1))
        self.ui.date_fin.setDate(QDate.currentDate())
        self.ui.date_mois.setDate(QDate.currentDate())
        self.ui.date_annee.setDate(QDate.currentDate())

        self.ui.choix_produit.currentIndexChanged.connect(self._produit_change)
        self.ui.btn_rechercher.clicked.connect(self._rechercher)
        self.ui.mode.currentIndexChanged.connect(self._basculer_mode)
        self.ui.date_debut.dateChanged.connect(self.afficher_mouvements)
        self.ui.date_fin.dateChanged.connect(self.afficher_mouvements)
        self.ui.date_mois.dateChanged.connect(self.afficher_mouvements)
        self.ui.date_annee.dateChanged.connect(self.afficher_mouvements)

        self._basculer_mode()
        self.remplir_produits()
        self.afficher_mouvements()

    def remplir_produits(self):
        self.ui.choix_produit.blockSignals(True)
        self.ui.choix_produit.clear()
        self.ui.choix_produit.addItem("", "")
        for produit in db.product_lists():
            self.ui.choix_produit.addItem(
                f"{produit['NumProduit']} - {produit['Design']}",
                produit["NumProduit"],
            )
        self.ui.choix_produit.blockSignals(False)

    def _charger_produit(self, num_produit):
        return db.execute_one(
            "SELECT NumProduit, Design, Stock FROM Produit WHERE NumProduit = %s",
            (num_produit,),
        )

    def _produit_change(self):
        num_produit = self.ui.choix_produit.currentData()
        if not num_produit:
            self.produit_courant = None
            self.afficher_mouvements()
            return
        self.produit_courant = self._charger_produit(num_produit)
        self.afficher_mouvements()

    def _rechercher(self):
        texte = self.ui.choix_produit.currentText().strip()
        if not texte:
            QMessageBox.information(
                self, "Recherche", "Saisissez un numéro ou une désignation de produit."
            )
            return

        resultats = db.search_product(texte)
        if not resultats:
            QMessageBox.warning(
                self,
                "Produit non trouvé",
                f"Aucun produit ne correspond à « {texte} ».",
            )
            return

        if len(resultats) == 1:
            self._selectionner(resultats[0])
            return

        libelles = [f"{p['NumProduit']} - {p['Design']}" for p in resultats]
        choix, valide = QInputDialog.getItem(
            self,
            "Plusieurs résultats",
            f"{len(resultats)} produits trouvés. Lequel voulez-vous afficher ?",
            libelles,
            0,
            False,
        )
        if not valide or not choix:
            return
        for produit in resultats:
            if f"{produit['NumProduit']} - {produit['Design']}" == choix:
                self._selectionner(produit)
                return

    def _selectionner(self, produit):
        self.produit_courant = produit
        index = self.ui.choix_produit.findData(produit["NumProduit"])
        if index >= 0:
            self.ui.choix_produit.blockSignals(True)
            self.ui.choix_produit.setCurrentIndex(index)
            self.ui.choix_produit.blockSignals(False)
        self.afficher_mouvements()

    def rafraichir(self):
        self.remplir_produits()
        if self.produit_courant is not None:
            index = self.ui.choix_produit.findData(self.produit_courant["NumProduit"])
            if index >= 0:
                self.ui.choix_produit.blockSignals(True)
                self.ui.choix_produit.setCurrentIndex(index)
                self.ui.choix_produit.blockSignals(False)
        self.afficher_mouvements()

    def _basculer_mode(self):
        mode = self.ui.mode.currentIndex()
        self.ui.date_debut.setEnabled(mode == MODE_INTERVALLE)
        self.ui.date_fin.setEnabled(mode == MODE_INTERVALLE)
        self.ui.date_mois.setEnabled(mode == MODE_MOIS)
        self.ui.date_annee.setEnabled(mode == MODE_ANNEE)
        self.afficher_mouvements()

    def _periode(self):
        mode = self.ui.mode.currentIndex()

        if mode == MODE_INTERVALLE:
            debut = self.ui.date_debut.date()
            fin = self.ui.date_fin.date()
            d1 = date(debut.year(), debut.month(), debut.day())
            d2 = date(fin.year(), fin.month(), fin.day())
            if d1 > d2:
                d1, d2 = d2, d1
            return d1, d2, f"du {d1.strftime('%d/%m/%Y')} au {d2.strftime('%d/%m/%Y')}"

        if mode == MODE_MOIS:
            mois = self.ui.date_mois.date()
            d1 = date(mois.year(), mois.month(), 1)
            dernier_jour = monthrange(mois.year(), mois.month())[1]
            d2 = date(mois.year(), mois.month(), dernier_jour)
            return d1, d2, f"mois de {d1.strftime('%m/%Y')}"

        if mode == MODE_ANNEE:
            annee = self.ui.date_annee.date().year()
            return date(annee, 1, 1), date(annee, 12, 31), f"année {annee}"

        return None, None, "tout l'historique"

    @staticmethod
    def _format_jour(jour):
        if jour is None:
            return ""
        if hasattr(jour, "strftime"):
            return jour.strftime("%d/%m/%Y")
        return str(jour)

    def _mouvements(self, num_produit, debut, fin):
        filtre_entree = "NumProduit = %s"
        params_entree = [num_produit]
        filtre_sortie = "NumProduit = %s"
        params_sortie = [num_produit]

        if debut is not None:
            filtre_entree += " AND DateEntree BETWEEN %s AND %s"
            params_entree += [debut, fin]
            filtre_sortie += " AND DateSortie BETWEEN %s AND %s"
            params_sortie += [debut, fin]

        mouvements = []
        for ligne in db.execute(
            f"SELECT NumBon, QteEntree, DateEntree FROM BondeEntree "
            f"WHERE {filtre_entree}",
            tuple(params_entree),
            fetch=True,
        ):
            mouvements.append(
                {
                    "NumBon": ligne["NumBon"],
                    "Entree": ligne["QteEntree"],
                    "Sortie": None,
                    "Jour": ligne["DateEntree"],
                }
            )

        for ligne in db.execute(
            f"SELECT NumBon, QteSortie, DateSortie FROM BondeSortie "
            f"WHERE {filtre_sortie}",
            tuple(params_sortie),
            fetch=True,
        ):
            mouvements.append(
                {
                    "NumBon": ligne["NumBon"],
                    "Entree": None,
                    "Sortie": ligne["QteSortie"],
                    "Jour": ligne["DateSortie"],
                }
            )

        mouvements.sort(key=lambda m: (m["Jour"], m["NumBon"]), reverse=True)
        return mouvements

    def afficher_mouvements(self):
        if self.produit_courant is None:
            num_produit = self.ui.choix_produit.currentData()
            if num_produit:
                self.produit_courant = self._charger_produit(num_produit)

        if self.produit_courant is None:
            tbm.fill_table(self.ui.table, [])
            self.ui.periode.setText("Période : -")
            self.ui.lbl_num.setText("-")
            self.ui.lbl_design.setText("-")
            self.ui.lbl_stock.setText("-")
            self.ui.resume.setText(
                "Sélectionnez un produit pour afficher ses mouvements."
            )
            return

        num_produit = self.produit_courant["NumProduit"]
        produit = self._charger_produit(num_produit)
        if produit is None:
            QMessageBox.warning(
                self,
                "Produit non trouvé",
                f"Le produit « {num_produit} » n'existe plus.",
            )
            self.produit_courant = None
            self.afficher_mouvements()
            return
        self.produit_courant = produit

        debut, fin, libelle = self._periode()
        self.ui.periode.setText(f"Période : {libelle}")

        mouvements = self._mouvements(num_produit, debut, fin)
        tbm.fill_table(
            self.ui.table,
            [
                [
                    mouvement["NumBon"],
                    mouvement["Entree"] or "",
                    mouvement["Sortie"] or "",
                    self._format_jour(mouvement["Jour"]),
                ]
                for mouvement in mouvements
            ],
        )

        total_entree = sum(mouvement["Entree"] or 0 for mouvement in mouvements)
        total_sortie = sum(mouvement["Sortie"] or 0 for mouvement in mouvements)

        self.ui.lbl_num.setText(str(num_produit))
        self.ui.lbl_design.setText(str(produit["Design"]))
        self.ui.lbl_stock.setText(str(produit["Stock"]))
        self.ui.resume.setText(
            f"Total Entrée : {total_entree} &nbsp;•&nbsp; Total Sortie : {total_sortie} "
            f"&nbsp;•&nbsp; Solde des mouvements : {total_entree - total_sortie} "
            f"&nbsp;•&nbsp; {len(mouvements)} mouvement(s) affiché(s)"
        )