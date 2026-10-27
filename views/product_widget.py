
from PySide6.QtWidgets import QWidget , QTableWidgetItem , QHeaderView , QDialog , QMessageBox
from PySide6.QtCore import QDate
from ui_compiled.ui_product_widget import Ui_ProductWidget
import db
from views import product_dialog
from utils.table_management import fill_table
import utils.table_management as tbm
from views.product_dialog import AddProductDialog
class ProductWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProductWidget()
        self.ui.setupUi(self)
        tbm.columns_setting(self.ui.productTable, [160, 0, 110], stretch_column=1)
        self.ui.productTable.verticalHeader().setVisible(False)
        self.set_product_table()
        self.ui.btnSearch.clicked.connect(self.set_product_table)
        self.ui.btnAdd.clicked.connect(self.add_product)
        self.ui.btnDelete.clicked.connect(self.delete_product)
        self.ui.btnEdit.clicked.connect(self.edit_product)
    
    
    def set_product_table(self):
        products = db.product_lists()
        keywords = self.ui.searchInput.text()
        if keywords:
            filtered_products = [pr for pr in products if keywords.lower() in pr.get("NumProduit").lower() or keywords.lower() in pr.get("Design").lower()]
        else:
            filtered_products = products
        
        tbm.fill_table(
        self.ui.productTable,
        [
            [product["NumProduit"], product["Design"], product["Stock"]]
                for product in filtered_products
            ],
        )

    def add_product(self):
        products = db.product_lists()
        num_product = int(products[-1].get('NumProduit')[4:]) + 1
        dialog = AddProductDialog(self)
        dialog.ui.numProdInput.setText(f"PRD-{str(num_product).zfill(4)}")
        dialog.ui.numProdInput.setReadOnly(True)
        if dialog.exec() == QDialog.Accepted:
            num_product , designation , stock = dialog.get_dialog_data()
            if designation.strip().lower() in [pr.get("Design").strip().lower() for pr in products]:
                QMessageBox.warning(self , "Attention" , "Le produit existe déja")
                return
            else:
                db.add_product(num_product , designation , stock)
                self.set_product_table()

    def delete_product(self):
        row = self.ui.productTable.currentRow()
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmation")
        if row == -1 :
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner une ligne")
            return
        else:
            num_product = self.ui.productTable.item(row , 0).text()
            dialog.setInformativeText(f"Voulez vous vraiment supprimer le produit {num_product}")
            dialog.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
            if dialog.exec() == QMessageBox.StandardButton.Yes:
                db.delete_product(num_product)
                self.set_product_table()
                QMessageBox.information(self, "Succès", "Suppression réussi !")


    def edit_product(self):
        row = self.ui.productTable.currentRow()
        if row == -1 :
            QMessageBox.warning(self , "Attention" , "Veuillez selectionner une ligne")
            return
        dialog = AddProductDialog(self)
        dialog.setWindowTitle("Confirmation")
        dialog.ui.numProdInput.setReadOnly(True)
        dialog.ui.stockInput.setReadOnly(True)

        num_product = self.ui.productTable.item(row , 0).text()
        designation = self.ui.productTable.item(row , 1).text()
        stock = self.ui.productTable.item(row , 2).text()

        dialog.ui.numProdInput.setText(num_product)
        dialog.ui.designationInput.setText(designation)
        dialog.ui.stockInput.setValue(int(stock))

        if dialog.exec() == QDialog.Accepted:
            new_num_product , new_designation , new_stock = dialog.get_dialog_data()
            products = db.product_lists()
            if new_designation.lower().strip() == designation.lower().strip():
                QMessageBox.warning(self , "Attention" , "Vous n'avez effectué aucune modification.")
                return
            if any(
                pr.get("Design", "").strip().lower() == new_designation.strip().lower()
                and pr.get("NumProduit") != new_num_product
                for pr in products
            ):   
                QMessageBox.warning(self , "Attention" , "Le produit existe déja")
                return
            db.update_product(new_num_product , new_designation , new_stock)
            self.set_product_table()
            QMessageBox.information(self , "Succès" , "Modification réussie")




