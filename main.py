from views.main_window import MainWindow
import sys
from PySide6.QtWidgets import QApplication
from pathlib import Path
from PySide6.QtGui import QFont, QFontDatabase

BASE_DIR = Path(__file__).resolve().parent
FONT_DIR = BASE_DIR / "assets" / "fonts"

app = QApplication(sys.argv)

from PySide6.QtGui import QColor, QPalette

light_palette = app.palette()
for role in (
    QPalette.ColorRole.Window,
    QPalette.ColorRole.Base,
    QPalette.ColorRole.Button,
    QPalette.ColorRole.AlternateBase,
    QPalette.ColorRole.ToolTipBase,
):
    light_palette.setColor(role, QColor("#ffffff"))
for role in (
    QPalette.ColorRole.WindowText,
    QPalette.ColorRole.Text,
    QPalette.ColorRole.ButtonText,
    QPalette.ColorRole.ToolTipText,
):
    light_palette.setColor(role, QColor("#111827"))
app.setPalette(light_palette)

for font_file in FONT_DIR.glob("*.ttf"):
    font_id = QFontDatabase.addApplicationFont(str(font_file))

    if font_id == -1:
        print(f"Impossible de charger la police : {font_file.name}")

app.setFont(QFont("Montserrat", 10))

w = MainWindow()
w.show()
sys.exit(app.exec())



