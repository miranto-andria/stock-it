
from tkinter import dialog

from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_product_widget import Ui_productWidget
import db
from views import product_dialog
from views.entry_dialog import AddEntryDialog
from utils.table_management import fill_table
import utils.table_management as tbm
from views.product_dialog import AddProductDialog
class ProductWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_productWidget()
        self.ui.setupUi(self)
        tbm.columns_setting(self.ui.productTable, [160, 0, 110], colonne_etirable=1)
        self.ui.productTable.verticalHeader().setVisible(False)
        self.set_product_table()
        self.ui.btnAdd.clicked.connect(self.add_product)
        self.ui.btnDelete.clicked.connect(self.delete_product)
        self.ui.btnEdit.clicked.connect(self.edit_product)
    
    
    def set_product_table(self):
        produits = db.product_lists()
        tbm.fill_table(
        self.ui.productTable,
        [
            [produit["NumProduit"], produit["Design"], produit["Stock"]]
                for produit in produits
            ],
        )

    def add_product(self):
        produits = db.product_lists()
        num_produit = int(produits[-1].get('NumProduit')[4:]) + 1
        dialog = AddProductDialog()
        dialog.ui.numProdInput.setText(f"PRD-{str(num_produit).zfill(4)}")
        dialog.ui.numProdInput.setReadOnly(True)
        if dialog.exec() == QDialog.Accepted:
            NumProduit , Designation , Stock = dialog.get_dialog_data()
            if Designation.strip().lower() in [pr.get("Design").strip().lower() for pr in produits]:
                QMessageBox.warning(self , "Attention" , "Le produit existe déja")
                return
            else:
                db.add_product(NumProduit , Designation , Stock)
                self.set_product_table()

    def delete_product(self):
        row = self.ui.productTable.currentRow()
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmation")
        if row == -1 :
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner une ligne")
            return
        else:
            num_produit = self.ui.productTable.item(row , 0).text()
            dialog.setInformativeText(f"Voulez vous vraiment supprimer le produit {num_produit}")
            dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
            if dialog.exec() == QMessageBox.StandardButton.Yes:
                db.delete_product(num_produit)
                self.set_product_table()
                QMessageBox.information(self, "Succès", "Suppression réussi !")


    def edit_product(self):
        row = self.ui.productTable.currentRow()
        if row == -1 :
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner une ligne")
            return
        dialog = AddProductDialog()
        dialog.setWindowTitle("Confirmation")
        dialog.ui.numProdInput.setReadOnly(True)
        dialog.ui.stockInput.setReadOnly(True)

        num_produit = self.ui.productTable.item(row , 0).text()
        designation = self.ui.productTable.item(row , 1).text()
        stock = self.ui.productTable.item(row , 2).text()

        dialog.ui.numProdInput.setText(num_produit)
        dialog.ui.designationInput.setText(designation)
        dialog.ui.stockInput.setValue(int(stock))

        if dialog.exec() == QDialog.Accepted:
            NumProduit , Designation , Stock = dialog.get_dialog_data()
            products = db.product_lists()
            if Designation.lower().strip() == designation.lower().strip():
                QMessageBox.warning(self , "Attention" , "Vous n'avez effectué aucune modification.")
                return
            if any(
                pr.get("Design", "").strip().lower() == Designation.strip().lower()
                and pr.get("NumProduit") != NumProduit
                for pr in products
            ):   
                QMessageBox.warning(self , "Attention" , "Le produit existe déja")
                return
            db.update_product(NumProduit , Designation , Stock)
            self.set_product_table()
            QMessageBox.information(self , "Succès" , "Modification réussie")





