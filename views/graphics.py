
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QPieSeries,
    QPieSlice,
    QValueAxis,
)
from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QFrame

# Palette claire du dashboard (cartes et cadres blancs, accents bleus).
BG_PRIMARY = "#f8f8f8"
BG_SECONDARY = "#ffffff"
ACCENT = "#2d66e4"
TEXT_COLOR = "#111827"

# Couleurs secondaires
SOFT_TEXT_COLOR = "#374151"
AXIS_COLOR = "#6b7280"
GRID_COLOR = "#e5e7eb"
BAR_COLOR = ACCENT
BAR_BORDER_COLOR = "#2153c5"
BAR_HOVER_COLOR = "#4a80f0"

PALETTE = [
    "#2d66e4",
    "#774cff",
    "#0ea5e9",
    "#14b8a6",
    "#f59e0b",
    "#ec4899",
    "#22c55e",
    "#8b5cf6",
    "#f43f5e",
    "#6b7280",
]


def _truncate(text, size):
    text = str(text)
    if len(text) <= size:
        return text
    return text[:size - 3] + "..."


def _abbreviated_labels(labels):
    count = len(labels)
    if count == 0:
        return []

    size = max(7, min(22, 190 // count + 3))
    return [_truncate(label, size) for label in labels]


class BaseChart(QChartView):
    title = ""

    def __init__(self, parent=None):
        super().__init__(parent)

        self._data = []

        # Taille minimale revue : assez grande pour rester lisible
        # (25 produits dans l'histogramme), sans deborder de la page
        # (l'en-tete, les 4 cartes et le bloc des mouvements prennent le
        # reste) ; le stretch de la page fait grossir les graphiques au-dela.
        self.setMinimumSize(400, 250)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setStyleSheet(
            f"""
            QChartView {{
                background-color: {BG_SECONDARY};
                border: none;
                border-radius: 12px;
            }}
            """
        )
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        self.setChart(self._empty_chart())

    def set_data(self, data):
        self._data = [
            (str(label), float(value))
            for label, value in data
        ]
        self._build()

    def data(self):
        return list(self._data)

    def _empty_chart(self):
        chart = QChart()

        chart.setTitle(self.title)
        chart.setTitleFont(self._title_font())
        chart.setTitleBrush(QColor(TEXT_COLOR))

        chart.setBackgroundBrush(QColor(BG_SECONDARY))
        chart.setBackgroundRoundness(12)
        chart.setPlotAreaBackgroundBrush(QColor(BG_SECONDARY))
        chart.setPlotAreaBackgroundVisible(True)

        # Marge superieure generouse : les etiquettes exterieures du
        # camembert (tranche en haut) ne doivent pas passer sous le titre.
        chart.setMargins(QMargins(12, 28, 12, 8))
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        chart.legend().setVisible(False)

        return chart

    def _title_font(self):
        font = QFont(self.font())
        font.setBold(True)
        font.setPointSize(11)
        return font

    def _axis_font(self):
        font = QFont(self.font())
        font.setPointSize(8)
        return font

    def _build(self):
        raise NotImplementedError


class HistogramWidget(BaseChart):
    title = "État du stock par produit"

    def _build(self):
        chart = self._empty_chart()

        if not self._data:
            chart.setTitle(f"{self.title} - Aucune donnée")
            self.setChart(chart)
            return

        series = QBarSeries()
        series.setBarWidth(0.68)
        series.setLabelsVisible(True)
        series.setLabelsFormat("@value")
        series.setLabelsPrecision(10)

        bar_set = QBarSet("Stock")
        bar_set.setColor(QColor(BAR_COLOR))
        bar_set.setBorderColor(QColor(BAR_BORDER_COLOR))
        bar_set.setLabelFont(self._axis_font())
        bar_set.setLabelColor(QColor(TEXT_COLOR))

        for _, value in self._data:
            bar_set.append(value)

        series.append(bar_set)
        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(
            _abbreviated_labels([
                label for label, _ in self._data
            ])
        )
        axis_x.setLabelsFont(self._axis_font())
        axis_x.setLabelsColor(QColor(SOFT_TEXT_COLOR))
        axis_x.setGridLineVisible(False)
        axis_x.setLinePen(QPen(QColor(GRID_COLOR), 1))

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        maximum = max(
            (value for _, value in self._data),
            default=1
        )
        maximum = max(maximum, 1)

        axis_y = QValueAxis()
        axis_y.setRange(0, maximum * 1.18)
        axis_y.setTickCount(6)
        axis_y.setLabelFormat("%.0f")
        axis_y.setLabelsFont(self._axis_font())
        axis_y.setLabelsColor(QColor(AXIS_COLOR))
        axis_y.setGridLineColor(QColor(GRID_COLOR))
        axis_y.setLineVisible(False)
        axis_y.setMinorGridLineVisible(False)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        self.setChart(chart)


class PieChartWidget(BaseChart):
    title = "Répartition des produits par niveau de stock"

    def _build(self):
        chart = self._empty_chart()

        positive_data = [
            (label, value)
            for label, value in self._data
            if value > 0
        ]

        total = sum(value for _, value in positive_data)

        if not positive_data or total <= 0:
            chart.setTitle(f"{self.title} - Aucune donnée")
            self.setChart(chart)
            return

        series = QPieSeries()
        series.setPieSize(0.62)
        series.setHorizontalPosition(0.5)
        series.setVerticalPosition(0.48)

        series.setLabelsVisible(True)
        series.setLabelsPosition(
            QPieSlice.LabelPosition.LabelOutside
        )

        for index, (label, value) in enumerate(positive_data):
            percentage = 100 * value / total

            part = series.append(
                f"{label} : {value:.0f} ({percentage:.1f} %)",
                value
            )

            self._decorate(part, index)

        chart.addSeries(series)

        # La legende repete la meme donnée que les etiquettes exterieures :
        # on n'y laisse que le nom, pour eviter les ellipses du type
        # « Rupture(0) : 2 (8… » lors du calcul des proportions.
        for marqueur, (label, _valeur) in zip(
            chart.legend().markers(series), positive_data
        ):
            marqueur.setLabel(str(label))

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        chart.legend().setLabelColor(QColor(SOFT_TEXT_COLOR))
        chart.legend().setFont(self._axis_font())

        self.setChart(chart)

    def _decorate(self, part, index):
        part.setColor(
            QColor(PALETTE[index % len(PALETTE)])
        )
        part.setBorderColor(QColor(BG_SECONDARY))
        part.setBorderWidth(2)

        part.setLabelVisible(True)
        part.setLabelColor(QColor(TEXT_COLOR))
        part.setLabelFont(self._axis_font())
        part.setLabelArmLengthFactor(0.18)
