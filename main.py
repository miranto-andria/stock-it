from views.main_window import mainWindow
import sys
from PySide6.QtWidgets import QApplication



app = QApplication(sys.argv)

w = mainWindow()
w.show()
sys.exit(app.exec())



