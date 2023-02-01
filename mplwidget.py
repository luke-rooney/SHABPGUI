from PySide6.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig    = Figure()
        self.canvas = FigureCanvas(self.fig)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.axes = self.fig.add_subplot(111, projection='3d')
        self.setLayout(vertical_layout)

class MplCanvas2D(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.fig    = Figure()
        self.canvas = FigureCanvas(self.fig)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.axes = self.fig.add_subplot(111)
        self.setLayout(vertical_layout)