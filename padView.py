from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel, QCheckBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import sqlite3
import pandas as pd
import dirCalcs as dc
import UI.padViewUi as pvUi

class padView(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.pad = self.well.split('-')[0]
        self.showWell = []
        self.label = []
        self.highlight = []
        self.ui = pvUi.Ui_padView()
        self.threedWin = QMainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(250,355)
        self.getWells()
        self.generateBoxes()
        self.show()
        self.padThreed()
        return

    def getWells(self):
        self.wellDf = pd.DataFrame()
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        wells = []
        self.wellsDf = []
        data = cursor.execute(f"SELECT wellName FROM WELLS WHERE wellName like '{self.pad}%' ORDER BY wellName ASC")
        for item in data:
            for subItem in item:
                wells.append(subItem)
        j = 0
        for item in wells:
            self.wellsDf.append(pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{item}'", conn))
            data = cursor.execute(f"SELECT latitude, longitude FROM WELLS WHERE wellName = '{item}'")
            for item in data:
                lat, lon = item
            x, y = dc.latLon(lat, lon)
            self.wellsDf[j]['EW'] += x
            self.wellsDf[j]['NS'] += y
            j += 1 
        conn.close()
        return

    def generateBoxes(self):        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT DISTINCT wellName FROM DEV WHERE wellName LIKE '{self.pad}%' ORDER BY wellName ASC")
        i = 0
        j = 0
        k = 0
        h = 41
        for item in data:
            for subItem in item:
                if h < 331:
                    h += 22
                self.showWell.append(QCheckBox())
                self.ui.gridLayout.addWidget(self.showWell[i], i+1, 0, 1, 1, alignment=Qt.AlignCenter)
                self.showWell[i].setCheckState(Qt.CheckState.Checked)
                self.label.append(QLabel(f"{subItem}", self.ui.scrollAreaWidgetContents))
                self.ui.gridLayout.addWidget(self.label[j], j+1, 1, 1, 1, alignment=Qt.AlignCenter)
                self.highlight.append(QCheckBox())
                self.ui.gridLayout.addWidget(self.highlight[k], k+1, 2, 1, 1, alignment=Qt.AlignCenter)
                self.ui.scrollArea.setGeometry(QRect(10, 60, 173, h))
                if self.label[j].text() == self.well:
                    self.highlight[k].setCheckState(Qt.CheckState.Checked)
                self.showWell[i].stateChanged.connect(self.padThreed)
                self.highlight[k].stateChanged.connect(self.padThreed)
                i += 1
                j += 1
                k += 1
        return
    
    def showCheck(self):
        j = 0
        for item in self.showWell:
            if item.isChecked():
                self.ax3d.plot3D(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'],self.wellsDf[j]['TVD'], color='black')
            j += 1
        return
    
    def highlightCheck(self):
        j = 0
        for item in self.highlight:
            if item.isChecked() and self.showWell[j].isChecked():
                self.ax3d.plot3D(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'],self.wellsDf[j]['TVD'], color='red')
            else:
                item.setCheckState(Qt.CheckState.Unchecked)
            j += 1

        return
    
    def padThreed(self):
        self.fig3d = plt.Figure(figsize=(7.5,7.5))
        self.canvas = FigureCanvasQTAgg(self.fig3d)
        self.ax3d = self.fig3d.add_subplot(projection="3d")
        self.threedWin.setCentralWidget(self.canvas)
        self.threedWin.setWindowTitle(f"3D View - {self.pad}")
        self.threedWin.move(450,50)
        self.ax3d.set_title(f"3D View - {self.pad} pad")
        self.ax3d.set_xlabel('<-West - East->')
        self.ax3d.set_ylabel('<-North - South->')
        self.ax3d.grid(True)
        self.ax3d.invert_zaxis()
        self.ax3d.view_init(azim=225, elev=30)
        self.ax3d.set_zlabel('TVD')
        self.ax3d.tick_params(labelbottom=False, labelleft = False)
        self.showCheck()
        self.highlightCheck()
        self.threedWin.show()
        return
    
    def closeEvent(self, event):
        self.threedWin.close()
        self.close()
        return 