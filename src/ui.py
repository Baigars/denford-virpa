from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt
from contour_plot import ContourWidget
from geometry import generate_simple_od_profile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Denford virpa – detaļas ģenerators")
        self.resize(900, 600)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        control_layout = QVBoxLayout()
        main_layout.addLayout(control_layout, 0)

        self.stock_d_edit = QLineEdit("40")
        self.part_d_edit = QLineEdit("30")
        self.length_edit = QLineEdit("80")

        control_layout.addWidget(QLabel("Roundstock Ø"))
        control_layout.addWidget(self.stock_d_edit)
        control_layout.addWidget(QLabel("Detaļas Ø"))
        control_layout.addWidget(self.part_d_edit)
        control_layout.addWidget(QLabel("Detaļas garums"))
        control_layout.addWidget(self.length_edit)

        self.btn_update = QPushButton("Generate contour")
        self.btn_update.clicked.connect(self.update_contour)
        control_layout.addWidget(self.btn_update)
        control_layout.addStretch(1)

        self.contour_widget = ContourWidget()
        main_layout.addWidget(self.contour_widget, 1)

        self.update_contour()

    def update_contour(self):
        try:
            stock_d = float(self.stock_d_edit.text())
            part_d = float(self.part_d_edit.text())
            length = float(self.length_edit.text())
        except ValueError:
            return

        stock_radius = stock_d / 2.0
        profile = generate_simple_od_profile(part_d, length)
        self.contour_widget.update_geometry(stock_radius, profile)
