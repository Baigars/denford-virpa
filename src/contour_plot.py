from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ContourWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot(111)
        self.stock_radius = 0.0
        self.profile = []
        self.redraw()

    def update_geometry(self, stock_radius, profile_points):
        self.stock_radius = stock_radius
        self.profile = profile_points
        self.redraw()

    def redraw(self):
        self.ax.clear()
        if self.stock_radius > 0:
            xs = [0, 0, 0, 0]
            ys = [0, self.stock_radius, -self.stock_radius, 0]
            self.ax.plot(xs, ys, color="lightgray", linewidth=8, alpha=0.4)

        if self.profile:
            xs = [p[0] for p in self.profile]
            ys = [p[1] for p in self.profile]
            self.ax.plot(xs, ys, color="yellow", linewidth=2)

        self.ax.set_aspect("equal", adjustable="datalim")
        self.ax.grid(True, linestyle="--", alpha=0.3)
        self.ax.set_xlabel("X (garums)")
        self.ax.set_ylabel("R (radius)")
        self.canvas.draw()
