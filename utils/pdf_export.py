
from datetime import datetime

from PySide6.QtCore import Qt, QRectF, QMarginsF
from PySide6.QtGui import (
    QPdfWriter,
    QPainter,
    QFont,
    QColor,
    QPen,
    QPageSize,
    QPageLayout,
)
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase

def load_montserrat():
    fonts_dir = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "fonts"
    )

    for font_file in fonts_dir.glob("*.ttf"):
        QFontDatabase.addApplicationFont(str(font_file))
        
def from_table(parent, table):
    load_montserrat()
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Exporter le stock en PDF",
        "Stock_IT_rapport.pdf",
        "Fichiers PDF (*.pdf)"
    )

    if not file_path:
        return

    if not file_path.lower().endswith(".pdf"):
        file_path += ".pdf"

    try:
        headers = []
        for column in range(table.columnCount()):
            item = table.horizontalHeaderItem(column)
            headers.append(
                item.text() if item else f"Colonne {column + 1}"
            )

        rows_data = []
        for row in range(table.rowCount()):
            if table.isRowHidden(row):
                continue

            values = []
            for column in range(table.columnCount()):
                item = table.item(row, column)
                values.append(item.text() if item else "")

            rows_data.append(values)

        if not headers:
            QMessageBox.warning(
                parent, "Stock IT", "Le tableau ne contient aucune colonne."
            )
            return

        pdf = QPdfWriter(file_path)
        pdf.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
        pdf.setPageOrientation(QPageLayout.Orientation.Landscape)
        pdf.setResolution(96)
        pdf.setTitle("Stock IT - Rapport de stock")
        pdf.setCreator("Stock IT")

        margins = QMarginsF(12, 15, 12, 15)
        pdf.setPageMargins(margins, QPageLayout.Unit.Millimeter)

        painter = QPainter()
        if not painter.begin(pdf):
            raise RuntimeError("Impossible de démarrer la création du PDF.")

        try:
            width = pdf.width()
            height = pdf.height()

            purple = QColor("#6243FF")
            background = QColor("#13141F")
            text = QColor("#252638")
            light_text = QColor("#FFFFFF")
            line_color = QColor("#D9D9E5")
            even_background = QColor("#F1F2F8")
            odd_background = QColor("#FFFFFF")

            left_margin = 0
            right_margin = width
            y = 0
            page = 1

            title_height = 42
            subtitle_height = 25
            header_height = 32
            row_height = 28
            footer_height = 24

            def draw_header():
                nonlocal y

                painter.fillRect(
                    QRectF(0, 0, width, title_height + 10),
                    background
                )

                painter.setPen(light_text)
                painter.setFont(QFont("Montserrat", 17, QFont.Weight.Bold))
                painter.drawText(
                    QRectF(12, 5, width - 24, 28),
                    Qt.AlignmentFlag.AlignVCenter,
                    "STOCK IT"
                )

                painter.setFont(QFont("Montserrat", 9))
                painter.setPen(QColor("#C5C6D8"))
                painter.drawText(
                    QRectF(12, 32, width - 24, 18),
                    Qt.AlignmentFlag.AlignVCenter,
                    "Rapport de stock - "
                    + datetime.now().strftime("%d/%m/%Y à %H:%M")
                )

                y = title_height + subtitle_height

            def draw_footer():
                painter.setPen(QPen(purple, 1.5))
                painter.drawLine(
                    0, height - footer_height,
                    width, height - footer_height
                )
                painter.setPen(QColor("#77788D"))
                painter.setFont(QFont("Montserrat", 8))
                painter.drawText(
                    QRectF(0, height - footer_height + 3, width, 18),
                    Qt.AlignmentFlag.AlignCenter,
                    f"Stock IT | Page {page}"
                )

            def draw_row(values, row_y, height, is_header=False, index=0):
                column_count = len(headers)
                column_width = width / column_count

                for column, value in enumerate(values):
                    x = column * column_width
                    rect = QRectF(
                        x, row_y, column_width, height
                    )

                    if is_header:
                        background_color = purple
                        text_color = light_text
                        font = QFont("Montserrat", 9, QFont.Weight.Bold)
                    else:
                        background_color = (
                            even_background if index % 2 == 0 else odd_background
                        )
                        text_color = text
                        font = QFont("Montserrat", 9)

                    painter.fillRect(rect, background_color)
                    painter.setPen(QPen(line_color, 0.7))
                    painter.drawRect(rect)

                    painter.setPen(text_color)
                    painter.setFont(font)

                    cell_text = painter.fontMetrics().elidedText(
                        str(value),
                        Qt.TextElideMode.ElideRight,
                        max(10, int(column_width - 12))
                    )

                    painter.drawText(
                        rect.adjusted(6, 2, -6, -2),
                        Qt.AlignmentFlag.AlignVCenter
                        | Qt.AlignmentFlag.AlignLeft,
                        cell_text
                    )

            draw_header()
            draw_row(headers, y, header_height, is_header=True)
            y += header_height

            for index, values in enumerate(rows_data):
                if y + row_height > height - footer_height:
                    draw_footer()
                    pdf.newPage()
                    page += 1
                    draw_header()
                    draw_row(
                        headers, y, header_height, is_header=True
                    )
                    y += header_height

                draw_row(
                    values, y, row_height, index=index
                )
                y += row_height

            draw_footer()

        finally:
            painter.end()

        QMessageBox.information(
            parent,
            "Stock IT",
            f"Export PDF réussi :\n{file_path}"
        )

    except Exception as error:
        QMessageBox.critical(
            parent,
            "Erreur d'export",
            f"Impossible de générer le PDF :\n{error}"
        )
