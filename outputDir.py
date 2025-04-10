from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd
import sqlite3
import UI.outputDirReportUI as outUi



class outputDirPdf(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.ui = outUi.Ui_MainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,355)

        self.show()