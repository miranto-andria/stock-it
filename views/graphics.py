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

PALETTE = [
    "#2563eb",
    "#0ea5e9",
    "#14b8a6",
    "#f59e0b",
    "#ef4444",
    "#8b5cf6",
    "#ec4899",
    "#64748b",
]

BACKGROUND_COLOR = "#ffffff"
TEXT_COLOR = "#0f172a"
SOFT_TEXT_COLOR = "#475569"
AXIS_COLOR = "#64748b"
GRID_COLOR = "#e2e8f0"
BAR_COLOR = "#2563eb"
BAR_LIGHT_COLOR = "#60a5fa"


def _truncate(text, size):
    text = str(text)
    if len(text) <= size:
        return text
    return text[: size - 1] + "..."


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

        self.setMinimumSize(420, 300)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.setChart(self._empty_chart())

    def set_data(self, data):
        self._data = [(str(label), float(value)) for label, value in data]
        self._build()

    def data(self):
        return list(self._data)

    def _empty_chart(self):
        chart = QChart()
        chart.setTitle(self.title)
        chart.setTitleFont(self._title_font())
        chart.setTitleBrush(QColor(TEXT_COLOR))
        chart.setBackgroundBrush(QColor(BACKGROUND_COLOR))
        chart.setBackgroundRoundness(0)
        chart.setPlotAreaBackgroundVisible(False)
        chart.setMargins(QMargins(16, 16, 16, 12))
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
    title = "État de stock par produit"

    def _build(self):
        chart = self._empty_chart()

        if not self._data:
            chart.setTitle(self.title + " - no data")
            self.setChart(chart)
            return

        series = QBarSeries()
        series.setBarWidth(0.72)
        series.setLabelsVisible(True)
        series.setLabelsFormat("@value")
        series.setLabelsPrecision(10)

        bar_set = QBarSet("Stock")
        bar_set.setColor(QColor(BAR_COLOR))
        bar_set.setBorderColor(QColor(BAR_LIGHT_COLOR))
        bar_set.setLabelFont(self._axis_font())
        bar_set.setLabelColor(QColor(TEXT_COLOR))
        for _, value in self._data:
            bar_set.append(value)
        series.append(bar_set)
        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(_abbreviated_labels([label for label, _ in self._data]))
        axis_x.setLabelsFont(self._axis_font())
        axis_x.setLabelsColor(QColor(AXIS_COLOR))
        axis_x.setGridLineVisible(False)
        axis_x.setLinePen(QPen(QColor(GRID_COLOR), 1))
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        maximum = max((value for _, value in self._data), default=1) or 1
        axis_y = QValueAxis()
        axis_y.setRange(0, maximum * 1.15)
        axis_y.setTickCount(6)
        axis_y.setLabelFormat("%.0f")
        axis_y.setLabelsFont(self._axis_font())
        axis_y.setLabelsColor(QColor(AXIS_COLOR))
        axis_y.setGridLineColor(QColor(GRID_COLOR))
        axis_y.setLineVisible(False)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        self.setChart(chart)


class PieChartWidget(BaseChart):
    title = "Répartition des produits par niveau de stock"

    def _build(self):
        chart = self._empty_chart()

        series = QPieSeries()
        series.setPieSize(0.70)
        series.setVerticalPosition(0.56)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)

        total = sum(value for _, value in self._data if value > 0)
        parts = 0
        for index, (label, value) in enumerate(self._data):
            if value <= 0:
                continue
            percentage = 100 * value / total
            part = series.append(f"{label} : {value:.0f} ({percentage:.0f} %)", value)
            self._decorate(part, index)
            parts += 1

        if parts == 0:
            chart.setTitle(self.title + " - no data")
            self.setChart(chart)
            return

        chart.addSeries(series)
        self.setChart(chart)

    def _decorate(self, part, index):
        part.setColor(QColor(PALETTE[index % len(PALETTE)]))
        part.setBorderColor(QColor(BACKGROUND_COLOR))
        part.setBorderWidth(2)
        part.setLabelVisible(True)
        part.setLabelColor(QColor(SOFT_TEXT_COLOR))
        part.setLabelFont(self._axis_font())
        part.setLabelArmLengthFactor(0.18)