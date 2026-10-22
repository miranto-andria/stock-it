
from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_exit_widget import Ui_exitWidget
import db
from views.entry_dialog import AddEntryDialog
from ui_compiled.ui_add_entry_dialog import Ui_Dialog
from utils.table_management import fill_table

class ExitWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_exitWidget()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.set_exit_table)
        self.set_exit_table()
        self.ui.btnAdd.clicked.connect(self.show_add_dialog)
        self.ui.btnDelete.clicked.connect(self.delete_row)
        self.ui.btnEdit.clicked.connect(self.edit_row)

    def set_exit_table(self):
        exit_passes = db.get_exit_pass()
        keywords = self.ui.searchInput.text() 
        self.ui.exitTable.setColumnWidth(0 , 200)
        self.ui.exitTable.setColumnWidth(1 , 100)
        self.ui.exitTable.setColumnWidth(2 , 300)
        header = self.ui.exitTable.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch) 
        if keywords: 
            self.filtered_passes = [ps for ps in exit_passes if keywords.lower() in ps.get("NumProduit").lower() or keywords.lower() in ps.get("NumBon").lower() or keywords.lower() in ps.get("Design").lower()]    
        else:
            self.filtered_passes = exit_passes

        fill_table(self.ui.exitTable , [[fp.get("NumBon") , fp.get("NumProduit") ,fp.get("Design") , fp.get("QteSortie") , fp.get("DateSortie")] for fp in self.filtered_passes])

    def show_add_dialog(self):
        dialog = AddEntryDialog(self)
        if dialog.exec() == QDialog.Accepted:
            NumBon, NumProduit, QteSortie, DateSortie = dialog.get_dialog_data()
            entry = db.get_exit_pass()
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
            if len(DateSortie) != 10:
                QMessageBox.warning(self, "Erreur", "Format de date invalide.")
                return
            try:
                db.add_entry(NumBon, NumProduit, QteSortie, DateSortie)
                QMessageBox.information(self, "Succès", "Ajout réussi !")

                self.set_exit_table()
            except Exception as e:
                QMessageBox.critical(self, "Erreur BDD", f"Impossible d'ajouter : {e}")      

    def delete_row(self):
        row = self.ui.exitTable.currentRow()
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmation")
        if row == -1:
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner le bon à supprimer")
            return
        else:
            num_bon = self.ui.exitTable.item(row , 0).text()
            num_produit = self.ui.exitTable.item(row , 1).text()
            qte_sortie = self.ui.exitTable.item(row , 2).text()
            dialog.setInformativeText(f"Voulez vous vraiment supprimer le bon {num_bon}")
            dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
              
            reponse =dialog.exec()
            if reponse == QMessageBox.StandardButton.Yes:
                db.delete_entry(num_bon , int(qte_sortie), num_produit )
                self.set_exit_table()
                QMessageBox.information(self, "Succès", "Suppression réussi !")
    def edit_row(self):
        row = self.ui.exitTable.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner le bon à modifier")
            return

        dialog = AddEntryDialog(self)
        dialog.ui.numBonInput.setReadOnly(True)
        

        num_bon = self.ui.exitTable.item(row, 0).text()
        num_produit = self.ui.exitTable.item(row, 1).text()
        qte_sortie = self.ui.exitTable.item(row, 2).text()
        


        date_str = self.ui.exitTable.item(row, 3).text()
        annee, mois, jour = map(int, date_str.split("-"))


        dialog.ui.numBonInput.setText(num_bon)
        dialog.ui.numProdInput.setText(num_produit)
        dialog.ui.qteInput.setValue(int(qte_sortie))
        dialog.ui.dateInput.setDate(QDate(annee, mois, jour))


        if dialog.exec() == QDialog.Accepted:
            NumBon, NumProduit, QteSortie, DateSortie = dialog.get_dialog_data()
            entry = db.get_exit_pass()
            produits_existants = [fp.get("NumProduit") for fp in entry]
            if (NumProduit == num_produit
            and str(QteSortie) == str(qte_sortie)
            and str(DateSortie) == str(date_str)):
                QMessageBox.warning(self,"Attention","Vous n'avez effectué aucune modification.")
                return
            if NumProduit not in produits_existants:
                QMessageBox.warning(self, "Erreur", f"Le produit '{NumProduit}' n'existe pas.")
                return
            if len(DateSortie) != 10:
                QMessageBox.warning(self, "Erreur", "Format de date invalide.")
                return
            try:
                db.update_entry(NumBon, NumProduit, QteSortie, DateSortie)
                self.set_exit_table()
                QMessageBox.information(self, "Succès", "Modification réussi !")
            except Exception as e:
                QMessageBox.critical(self, "Erreur BDD", f"Impossible d'ajouter : {e}")      
            
