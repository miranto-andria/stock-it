
from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_entry_widget import Ui_entryWidget
import db
from views.entry_dialog import AddEntryDialog
from ui_compiled.ui_add_entry_dialog import Ui_Dialog
from utils.table_management import fill_table
class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_entryWidget()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.set_entry_table)
        self.set_entry_table()
        self.ui.searchChoice.addItems(["Numero de bon" , "Numero du produit"])
        self.ui.btnAdd.clicked.connect(self.show_dialog)
        self.ui.btnDelete.clicked.connect(self.delete_row)
        self.ui.btnEdit.clicked.connect(self.edit_row)

    def set_entry_table(self):
        entry_passes = db.get_entry_pass()
        keywords = self.ui.searchInput.text() 
        self.ui.entryTable.setColumnWidth(0 , 300)
        self.ui.entryTable.setColumnWidth(1 , 300)
        header = self.ui.entryTable.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch) 
        if keywords: 
            if self.ui.searchChoice.currentText() == "Numero du produit":
                self.filtered_passes = [e for e in entry_passes if keywords.lower() in e.get("NumProduit").lower()]
            elif self.ui.searchChoice.currentText() == "Numero de bon":
                self.filtered_passes = [e for e in entry_passes if keywords.lower() in e.get("NumBon").lower()]
        else:
            self.filtered_passes = entry_passes

        fill_table(self.ui.entryTable , [[fp.get("NumBon") , fp.get("NumProduit") , fp.get("QteEntree") , fp.get("DateEntree")] for fp in self.filtered_passes])

    def show_dialog(self):
        dialog = AddEntryDialog(self)
        if dialog.exec() == QDialog.Accepted:
            NumBon, NumProduit, QteEntree, DateEntree = dialog.get_dialog_data()
            entry = db.get_entry_pass()
            bons_existants = [fp.get("NumBon") for fp in entry]
            produits_existants = [fp.get("NumProduit") for fp in entry]
            if len(NumBon) < 5 or not NumBon.startswith("BE-"):
                QMessageBox.warning(self, "Erreur", "Numéro de bon invalide (doit commencer par BE- et faire 5 caractères min).")
                return
            if NumBon in bons_existants:
                QMessageBox.warning(self, "Erreur", "Ce numéro de bon existe déjà dans la base !")
                return
            if NumProduit not in produits_existants:
                QMessageBox.warning(self, "Erreur", f"Le produit '{NumProduit}' n'existe pas.")
                return
            if len(DateEntree) != 10:
                QMessageBox.warning(self, "Erreur", "Format de date invalide.")
                return
            try:
                db.add_entry(NumBon, NumProduit, QteEntree, DateEntree)
                QMessageBox.information(self, "Succès", "Ajout réussi !")
                self.set_entry_table()
                self.init_count()
            except Exception as e:
                QMessageBox.critical(self, "Erreur BDD", f"Impossible d'ajouter : {e}")      

    def delete_row(self):
        row = self.ui.entryTable.currentRow()
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmation")
        if row == -1:
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner le bon à supprimer")
            return
        else:
            num_bon = self.ui.entryTable.item(row , 0).text()
            dialog.setInformativeText(f"Voulez vous vraiment supprimer le bon {num_bon}")
            dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
              
            reponse =dialog.exec()
            if reponse == QMessageBox.StandardButton.Yes:
                db.delete_entry(num_bon)
                self.set_entry_table()
    def edit_row(self):
        row = self.ui.entryTable.currentRow()
        if row == -1:
            QMessageBox.warning(self , "Attention" ,"Veuillez selectionner le bon à supprimer")
            return
        else:
            dialog = AddEntryDialog(self)
            num_bon = self.ui.entryTable.item(row , 0).text()
            num_produit = self.ui.entryTable.item(row , 1).text()
            qte_entree = self.ui.entryTable.item(row , 2).text()
            jour, mois, annee = map( int ,self.ui.entryTable.item(row , 3).text().split("-"))
        dialog.ui.numBonInput.setText(num_bon)
        dialog.ui.numProdInput.setText(num_produit)
        dialog.ui.qteInput.setValue(int(qte_entree))
        dialog.ui.dateInput.setDate(QDate(jour , mois , annee))
        if dialog.exec() == QDialog.Accepted:
            NumBon , NumProduit , QteEntree , DateEntree = dialog.get_dialog_data()
            db.update_entry(NumBon , NumProduit , QteEntree , DateEntree)
            self.set_entry_table()