from views.main_window import mainWindow
import sys
from PySide6.QtWidgets import QApplication
from pathlib import Path
from PySide6.QtGui import QFont, QFontDatabase

BASE_DIR = Path(__file__).resolve().parent
FONT_DIR = BASE_DIR / "assets" / "fonts"

app = QApplication(sys.argv)
qss_file = Path(__file__).parent / "styles" / "styles.qss"
app.setStyleSheet(qss_file.read_text(encoding="utf-8"))
for font_file in FONT_DIR.glob("*.ttf"):
    font_id = QFontDatabase.addApplicationFont(str(font_file))

    if font_id == -1:
        print(f"Impossible de charger la police : {font_file.name}")

app.setFont(QFont("Montserrat", 10))

w = mainWindow()
w.show()
sys.exit(app.exec())



