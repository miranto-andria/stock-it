from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QMessageBox, QTableWidgetItem


def fill_table(table, rows):
    sorting_enabled = table.isSortingEnabled()
    table.setSortingEnabled(False)
    table.setRowCount(0)
    for values in rows:
        row = table.rowCount()
        table.insertRow(row)
        for column, value in enumerate(values):
            if value is None:
                text = ""
            elif isinstance(value, float) and value.is_integer():
                text = str(int(value))
            else:
                text = str(value)
            item = QTableWidgetItem(text)
            if column and isinstance(value, (int, float)) and not isinstance(value, bool):
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            else:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            table.setItem(row, column, item)
    table.setSortingEnabled(sorting_enabled)

def columns_setting(table, widths, stretch_column):
    for column, width in enumerate(widths):
        if width:
            table.setColumnWidth(column, width)
    table.horizontalHeader().setSectionResizeMode(
        stretch_column, QHeaderView.ResizeMode.Stretch
    )
