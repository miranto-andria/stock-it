
from PySide6.QtWidgets import QWidget , QTableWidgetItem
from ui_compiled.ui_entry_widget import Ui_entryWidget
from db import get_entry_pass


class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_entryWidget()
        self.ui.setupUi(self)
        self.set_entry_table()

    def set_entry_table(self):
        entry_passes = get_entry_pass()
        row = self.ui.entryTable.rowCount()
        for entry_pass in entry_passes:
            self.ui.entryTable.insertRow(row)
            self.ui.entryTable.setItem(row , 1 , QTableWidgetItem(entry_pass.get("NumBon")))
            self.ui.entryTable.setItem(row , 2 , QTableWidgetItem(entry_pass.get("NumProduit")))
            self.ui.entryTable.setItem(row , 3 , QTableWidgetItem(str(entry_pass.get("QteEntree"))))
            self.ui.entryTable.setItem(row , 4 , QTableWidgetItem(str(entry_pass.get("DateEntree"))))
        