from PySide6.QtWidgets import QWidget , QTableWidgetItem
from ui_compiled.ui_entry_widget import Ui_entryWidget
from db import get_entry_pass


class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_entryWidget()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.set_entry_table)
        self.set_entry_table()
        self.ui.searchChoice.addItems(["Numero de bon" , "Numero du produit"])

    def set_entry_table(self):
        entry_passes = get_entry_pass()
        keywords = self.ui.searchInput.text()  
        if keywords: 
            if self.ui.searchChoice.currentText() == "Numero du produit":
                filtered_passes = [e for e in entry_passes if keywords.lower() in e.get("NumProduit").lower()]
            elif self.ui.searchChoice.currentText() == "Numero de bon":
                filtered_passes = [e for e in entry_passes if keywords.lower() in e.get("NumBon").lower()]
        else:
            filtered_passes = entry_passes

        self.ui.entryTable.setRowCount(0)
        self.ui.entryTable.setRowCount(len(filtered_passes))

        for row, entry_pass in enumerate(filtered_passes):
            self.ui.entryTable.insertRow(row)
            self.ui.entryTable.setItem(row , 0 , QTableWidgetItem(entry_pass.get("NumBon")))
            self.ui.entryTable.setItem(row , 1 , QTableWidgetItem(entry_pass.get("NumProduit")))
            self.ui.entryTable.setItem(row , 2 , QTableWidgetItem(str(entry_pass.get("QteEntree"))))
            self.ui.entryTable.setItem(row , 3 , QTableWidgetItem(str(entry_pass.get("DateEntree"))))
             
                