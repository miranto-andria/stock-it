
from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_entry_widget import Ui_EntryWidget
import db
from views.entry_dialog import AddEntryDialog
from utils.table_management import fill_table
class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EntryWidget()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.set_entry_table)
        self.set_entry_table()
        self.ui.btnAdd.clicked.connect(self.show_add_dialog)
        self.ui.btnDelete.clicked.connect(self.delete_row)
        self.ui.btnEdit.clicked.connect(self.edit_row)

    def set_entry_table(self):
        entry_passes = db.get_entry_pass()
        keywords = self.ui.searchInput.text() 
        self.ui.entryTable.setColumnWidth(0 , 200)
        self.ui.entryTable.setColumnWidth(1 , 100)
        self.ui.entryTable.setColumnWidth(2 , 300)
        header = self.ui.entryTable.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch) 
        if keywords: 
            self.filtered_passes = [ps for ps in entry_passes if keywords.lower() in ps.get("NumProduit").lower() or keywords.lower() in ps.get("NumBon").lower() or keywords.lower() in ps.get("Design").lower()]    
        else:
            self.filtered_passes = entry_passes

        fill_table(self.ui.entryTable , [[fp.get("NumBon") , fp.get("NumProduit") ,fp.get("Design") , fp.get("QteEntree") , fp.get("DateEntree")] for fp in self.filtered_passes])

    def show_add_dialog(self):
        dialog = AddEntryDialog(self)
        if dialog.exec() == QDialog.Accepted:
            new_num_voucher, new_num_product, new_entry_qty, new_entry_date = dialog.get_dialog_data()
            entry = db.get_entry_pass()
            existing_vouchers = [fp.get("NumBon") for fp in entry]
            existing_products = [fp.get("NumProduit") for fp in entry]
            if len(new_num_voucher) < 5 or not new_num_voucher.startswith("BE-"):
                QMessageBox.warning(self, "Erreur", "Numéro de bon invalide (doit commencer par BE- et faire 5 caractères min).")
                return
            if new_num_voucher in existing_vouchers:
                QMessageBox.warning(self, "Erreur", "Ce numéro de bon existe déjà dans la base !")
                return
            if new_num_product not in existing_products:
                QMessageBox.warning(self, "Erreur", f"Le produit '{new_num_product}' n'existe pas.")
                return
            if len(new_entry_date) != 10:
                QMessageBox.warning(self, "Erreur", "Format de date invalide.")
                return
            try:
                db.add_entry(new_num_voucher, new_num_product, new_entry_qty, new_entry_date)
                QMessageBox.information(self, "Succès", "Ajout réussi !")

                self.set_entry_table()
            except Exception as e:
                QMessageBox.critical(self, "Erreur BDD", f"Impossible d'ajouter : {e}")      

    def delete_row(self):
        row = self.ui.entryTable.currentRow()
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmation")
        if row == -1:
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner le bon à supprimer")
            return
        else:
            num_voucher = self.ui.entryTable.item(row , 0).text()
            num_product = self.ui.entryTable.item(row , 1).text()
            entry_qty = self.ui.entryTable.item(row , 3).text()
            dialog.setInformativeText(f"Voulez vous vraiment supprimer le bon {num_voucher}")
            dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
              
            answer =dialog.exec()
            if answer == QMessageBox.StandardButton.Yes:
                db.delete_entry(num_voucher , int(entry_qty), num_product )
                self.set_entry_table()
                QMessageBox.information(self, "Succès", "Suppression réussi !")
    def edit_row(self):
        row = self.ui.entryTable.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner le bon à modifier")
            return

        dialog = AddEntryDialog(self)
        dialog.ui.numBonInput.setReadOnly(True)
        

        num_voucher = self.ui.entryTable.item(row, 0).text()
        num_product = self.ui.entryTable.item(row, 1).text()
        entry_qty = self.ui.entryTable.item(row, 3).text()
        


        date_str = self.ui.entryTable.item(row, 4).text()
        year, month, day = map(int, date_str.split("-"))


        dialog.ui.numBonInput.setText(num_voucher)
        dialog.ui.numProdInput.setText(num_product)
        dialog.ui.qteInput.setValue(int(entry_qty))
        dialog.ui.dateInput.setDate(QDate(year, month, day))


        if dialog.exec() == QDialog.Accepted:
            new_num_voucher, new_num_product, new_entry_qty, new_entry_date = dialog.get_dialog_data()
            entry = db.get_entry_pass()
            existing_products = [fp.get("NumProduit") for fp in entry]
            if (new_num_product == num_product
            and str(new_entry_qty) == str(entry_qty)
            and str(new_entry_date) == str(date_str)):
                QMessageBox.warning(self,"Attention","Vous n'avez effectué aucune modification.")
                return
            if new_num_product not in existing_products:
                QMessageBox.warning(self, "Erreur", f"Le produit '{new_num_product}' n'existe pas.")
                return
            if len(new_entry_date) != 10:
                QMessageBox.warning(self, "Erreur", "Format de date invalide.")
                return
            try:
                db.update_entry(new_num_voucher, new_num_product, new_entry_qty, new_entry_date)
                self.set_entry_table()
                QMessageBox.information(self, "Succès", "Modification réussi !")
            except Exception as e:
                QMessageBox.critical(self, "Erreur BDD", f"Impossible d'ajouter : {e}")      
            
