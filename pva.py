from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd
import sqlite3
import UI.pvaUi as pvUi
import actual as ac



class planVsActual(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        
        self.ui = pvUi.Ui_pvaWindow()
        self.sectionWin = QMainWindow()
        self.planWin = QMainWindow()
        self.tvdWin = QMainWindow()
        self.threedWin = QMainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,355)
        
        self.ui.planBtn.clicked.connect(self.planned)
        self.ui.updateActualBtn.clicked.connect(self.updateActual)

        self.show()

    def planned(self):

        return

    def updateActual(self):
        self.acutalWin = ac.updateActual(self.well)
        return
    
    def closeEvent(self, event):
        self.acutalWin.close()
        self.close()
        return  