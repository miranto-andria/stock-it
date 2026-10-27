from calendar import monthrange
from datetime import date

from PySide6.QtCore import QDate
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QInputDialog, QMessageBox, QWidget

import db
import utils.table_management as tbm
from ui_compiled.ui_movement_widget import Ui_MovementWidget

MODE_RANGE = 0
MODE_MONTH = 1
MODE_YEAR = 2
MODE_ALL = 3


class MovementWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MovementWidget()
        self.ui.setupUi(self)

        self.current_product = None

        tbm.columns_setting(self.ui.table, [150, 120, 120, 0], stretch_column=3)
        self.ui.table.verticalHeader().setVisible(False)

        self.ui.date_debut.setDate(QDate.currentDate().addMonths(-1))
        self.ui.date_fin.setDate(QDate.currentDate())
        self.ui.date_mois.setDate(QDate.currentDate())
        self.ui.date_annee.setDate(QDate.currentDate())

        self.ui.btn_rechercher.clicked.connect(self._search)
        self.ui.mode.currentIndexChanged.connect(self._toggle_mode)
        self.ui.date_debut.dateChanged.connect(self.show_movements)
        self.ui.date_fin.dateChanged.connect(self.show_movements)
        self.ui.date_mois.dateChanged.connect(self.show_movements)
        self.ui.date_annee.dateChanged.connect(self.show_movements)

        self._toggle_mode()
        self.fill_products()
        self.show_movements()

    def fill_products(self):
        if self.current_product is None:
            self.ui.choix_produit.clear()

    def _load_product(self, num_product):
        return db.get_product(num_product)

    def _search(self):
        text = self.ui.choix_produit.text().strip()
        if not text:
            QMessageBox.information(
                self, "Recherche", "Saisissez un numéro ou une désignation de produit."
            )
            return

        results = db.search_product(text)
        if not results:
            QMessageBox.warning(
                self,
                "Produit non trouvé",
                f"Aucun produit ne correspond à « {text} ».",
            )
            return

        if len(results) == 1:
            self._select(results[0])
            return

        labels = [f"{p['NumProduit']} - {p['Design']}" for p in results]
        choice, ok = QInputDialog.getItem(
            self,
            "Plusieurs résultats",
            f"{len(results)} produits trouvés. Lequel voulez-vous afficher ?",
            labels,
            0,
            False,
        )
        if not ok or not choice:
            return
        for product in results:
            if f"{product['NumProduit']} - {product['Design']}" == choice:
                self._select(product)
                return

    def _select(self, product):
        self.current_product = product
        self.ui.choix_produit.setText(product["NumProduit"])
        self.show_movements()

    def refresh(self):
        self.fill_products()
        if self.current_product is not None:
            self.ui.choix_produit.setText(self.current_product["NumProduit"])
        self.show_movements()

    def _toggle_mode(self):
        mode = self.ui.mode.currentIndex()
        self.ui.date_debut.setEnabled(mode == MODE_RANGE)
        self.ui.date_fin.setEnabled(mode == MODE_RANGE)
        self.ui.date_mois.setEnabled(mode == MODE_MONTH)
        self.ui.date_annee.setEnabled(mode == MODE_YEAR)
        self.show_movements()

    def _period(self):
        mode = self.ui.mode.currentIndex()

        if mode == MODE_RANGE:
            start = self.ui.date_debut.date()
            end = self.ui.date_fin.date()
            d1 = date(start.year(), start.month(), start.day())
            d2 = date(end.year(), end.month(), end.day())
            if d1 > d2:
                d1, d2 = d2, d1
            return d1, d2, f"{d1.strftime('%d/%m/%y')} - {d2.strftime('%d/%m/%y')}"

        if mode == MODE_MONTH:
            month = self.ui.date_mois.date()
            d1 = date(month.year(), month.month(), 1)
            last_day = monthrange(month.year(), month.month())[1]
            d2 = date(month.year(), month.month(), last_day)
            return d1, d2, f"Mois : {d1.strftime('%m/%Y')}"

        if mode == MODE_YEAR:
            year = self.ui.date_annee.date().year()
            return date(year, 1, 1), date(year, 12, 31), f"Année : {year}"

        return None, None, "Tout l'historique"

    @staticmethod
    def _format_day(day):
        if day is None:
            return ""
        if hasattr(day, "strftime"):
            return day.strftime("%d/%m/%Y")
        return str(day)

    def _movements(self, num_product, start, end):
        return db.movements_summary(num_product, start, end)

    def show_movements(self):
        if self.current_product is None:
            text = self.ui.choix_produit.text().strip()
            num_product = text if text else None
            if num_product:
                self.current_product = self._load_product(num_product)

        if self.current_product is None:
            tbm.fill_table(self.ui.table, [])
            self.ui.periode.setText("-")
            self.ui.lbl_num.setText("-")
            self.ui.lbl_design.setText("-")
            self.ui.lbl_stock.setText("-")
            self.ui.resume.setText(
                "Sélectionnez un produit pour afficher ses mouvements."
            )
            return

        num_product = self.current_product["NumProduit"]
        product = self._load_product(num_product)
        if product is None:
            QMessageBox.warning(
                self,
                "Produit non trouvé",
                f"Le produit « {num_product} » n'existe plus.",
            )
            self.current_product = None
            self.show_movements()
            return
        self.current_product = product

        start, end, label = self._period()
        self.ui.periode.setText(label)

        summary = self._movements(num_product, start, end)
        movements = list(reversed(summary["movements"]))
        tbm.fill_table(
            self.ui.table,
            [
                [
                    movement["NumBon"],
                    movement["Entry"] or "",
                    movement["Exit"] or "",
                    self._format_day(movement["Day"]),
                ]
                for movement in movements
            ],
        )
        self._highlight_movements(movements)

        total_entries = summary["total_entries"]
        total_exits = summary["total_exits"]

        self.ui.lbl_num.setText(str(num_product))
        self.ui.lbl_design.setText(str(product["Design"]))
        self.ui.lbl_stock.setText(str(product["Stock"]))
        self.ui.resume.setText(
            f"<span style='color:#15803d;'>Total entrée : {total_entries}</span>"
            f"&nbsp;&nbsp;|&nbsp;&nbsp;"
            f"<span style='color:#b91c1c;'>Total sortie : {total_exits}</span>"
            f"&nbsp;&nbsp;|&nbsp;&nbsp;"
            f"Solde des mouvements : {total_entries - total_exits}"
            f"&nbsp;&nbsp;|&nbsp;&nbsp;{len(movements)} mouvement(s) affiché(s)"
        )

    def _highlight_movements(self, movements):
        for row, movement in enumerate(movements):
            column = 1 if (movement["Entry"] or 0) > 0 else 2
            color = QColor("#15803d" if column == 1 else "#b91c1c")
            item = self.ui.table.item(row, column)
            if item is not None:
                item.setForeground(color)
