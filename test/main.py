import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from Ui_Form import Ui_MainWindow
import mysql.connector

config = {
    'host': 'localhost',      # ou l'IP de votre serveur MySQL
    'user': 'root',           # votre nom d'utilisateur
    'password': '',
    'database': 'stock'
}


class Fenetre(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.productTable.setRowCount(0)
        self.conn = mysql.connector.connect(**config)
        self.cur = self.conn.cursor(dictionary=True)
        self.onBtnClick()


    def onBtnClick(self):
        self.cur.execute("SELECT p.design designation  , p.stock stock FROM produit p")
        products = self.cur.fetchall()
        for product in products:
            row = self.productTable.rowCount()
            self.productTable.insertRow(row)
            self.productTable.setItem(row , 0 , QTableWidgetItem(product.get("designation")))
            self.productTable.setItem(row , 1 , QTableWidgetItem(str(product.get("stock"))))


     



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Fenetre()
    w.show()

    sys.exit(app.exec())
