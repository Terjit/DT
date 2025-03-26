from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd
import sqlite3
import UI.pvaUi as pvUi
<<<<<<< HEAD
import actual as ac

=======
import updatePlanned as up
import updateActual as ua
>>>>>>> 9643a3c0a3ebc92bde83b6a0911e84090cacd830


class planVsActual(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.sw = False
        self.tw = False
        self.lines = []
        self.lines1 = []
        self.forms = []
        self.pullData()
        
        self.ui = pvUi.Ui_pvaWindow()
        self.sectionWin = QMainWindow()
        self.planWin = QMainWindow()
        self.tvdWin = QMainWindow()
        self.threedWin = QMainWindow()
        self.updateP = QMainWindow()
        self.updateA = QMainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,355)
        
        self.ui.updatePlanBtn.clicked.connect(self.upPlan)
        self.ui.updateActualBtn.clicked.connect(self.updateActual)
        self.ui.sectionBtn.clicked.connect(self.section)
        self.ui.tvdBtn.clicked.connect(self.tvdMd)
        self.ui.planBtn.clicked.connect(self.plan)
        self.ui.threedBtn.clicked.connect(self.threed)

        self.ui.formationsBox.stateChanged.connect(self.formations)
        self.show()

    def pullData(self):
        self.wellDf = pd.DataFrame()
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()        
        self.wellDf = pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{self.well}' AND Planned = 1", conn)
        self.wellA = pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{self.well}' AND Planned = 0", conn)
        self.formationData = cursor.execute(f"SELECT formationName, TVD FROM FORMATIONS WHERE wellName = '{self.well}' ORDER BY TVD ASC")
        self.formResults = self.formationData.fetchone()
        for item in self.formationData:
                self.forms.append(item)
        return

    def upPlan(self):
        self.updateP = up.updatePlanned(self.well)
        self.pullData()
        return

    def updateActual(self):
<<<<<<< HEAD
        self.acutalWin = ac.updateActual(self.well)
        return
    
    def closeEvent(self, event):
        self.acutalWin.close()
        self.close()
        return  
=======
        self.updateA = ua.updateActual(self.well)
        self.pullData()
        return
    
    def section(self):
        self.fig1 = plt.Figure(figsize=(7.5,7.5))
        self.canvas = FigureCanvasQTAgg(self.fig1)
        self.axs = self.fig1.add_subplot()
        self.sectionWin.setCentralWidget(self.canvas)
        self.sectionWin.setWindowTitle(f"Section View - {self.well}")
        self.sectionWin.move(450,50)
        self.axs.plot(self.wellDf['NS'], self.wellDf['TVD'], label = 'Planned')
        self.axs.plot(self.wellA['NS'], self.wellA['TVD'], color = 'red', linestyle = 'dashed', label = 'Actual')
        self.axs.set_title("Section View TVD vs N/S")
        self.axs.set_xlabel('South(-) | North(+)')
        self.axs.set_ylabel('True Vertical Depth [ft]')
        self.axs.grid(True)
        self.axs.invert_yaxis()
        self.axs.legend()
        xmin, xmax = self.axs.get_xlim()
        self.axs.set_xlim(xmin, xmax)
        if self.formResults: 
            for item in self.forms:
                self.lines.append(self.axs.hlines(item[1], -100000, 100000, colors='green', linestyles='dashed', linewidth=0.75, visible=False))
                if self.wellDf.iloc[-1]['NS'] > 0:
                    self.lines.append(self.axs.text(xmax, item[1], item[0], ha='right', va='bottom', fontsize=7.5, visible=False))
                else:
                    self.lines.append(self.axs.text(xmin, item[1], item[0], ha='left', va='bottom', fontsize=7.5, visible=False))
                if self.ui.formationsBox.isChecked():
                    for item in self.lines:
                        item.set_visible(True)
        self.sw = True
        self.sectionWin.show()
        return

    def tvdMd(self):
        self.fig2 = plt.Figure(figsize=(7.5,7.5))
        self.canvas2 = FigureCanvasQTAgg(self.fig2)
        self.ax2 = self.fig2.add_subplot()
        self.tvdWin.setCentralWidget(self.canvas2)
        self.tvdWin.setWindowTitle(f"TVD vs MD - {self.well}")
        self.tvdWin.move(470,70)
        self.ax2.plot(self.wellDf['MD'], self.wellDf['TVD'], label = 'Planned')
        self.ax2.plot(self.wellA['MD'], self.wellA['TVD'], color = 'red', linestyle = 'dashed', label = 'Actual')
        self.ax2.set_title("TVD vs MD")
        self.ax2.set_xlabel('Measure Depth [ft]')
        self.ax2.set_ylabel('True Vertical Depth [ft]')
        self.ax2.grid(True)
        self.ax2.invert_yaxis()
        self.ax2.legend()
        xmin2, xmax2 = self.ax2.get_xlim()
        self.ax2.set_xlim(xmin2, xmax2)
        if self.formResults:
            for item in self.forms:
                self.lines1.append(self.ax2.hlines(item[1], -100000, 100000, colors='green', linestyles='dashed', linewidth=0.75, visible=False))
                self.lines1.append(self.ax2.text(xmax2, item[1], item[0], ha='right', va='bottom', fontsize=7.5, visible=False))
                if self.ui.formationsBox.isChecked():
                    for item in self.lines1:
                        item.set_visible(True)
        self.tw = True
        self.tvdWin.show()
        return

    def plan(self):
        self.figp = plt.Figure(figsize=(7.5,7.5))
        self.canvas = FigureCanvasQTAgg(self.figp)
        self.axp = self.figp.add_subplot()
        self.planWin.setCentralWidget(self.canvas)
        self.planWin.setWindowTitle(f"Plan View - {self.well}")
        self.planWin.move(490,90)
        self.axp.plot(self.wellDf['EW'], self.wellDf['NS'], label = 'Actual')
        self.axp.plot(self.wellA['EW'], self.wellA['NS'], color = 'red', linestyle = 'dashed', label = 'Planned')
        self.axp.set_title("Plan View")
        self.axp.set_xlabel('West(-) | East(+)')
        self.axp.set_ylabel('South(-) | North(+)')
        self.axp.grid(True)
        self.axp.legend()
        self.planWin.show()
        return

    def threed(self):
        self.fig3d = plt.Figure(figsize=(7.5,7.5))
        self.canvas = FigureCanvasQTAgg(self.fig3d)
        self.ax3d = self.fig3d.add_subplot(projection="3d")
        self.threedWin.setCentralWidget(self.canvas)
        self.threedWin.setWindowTitle(f"3D View - {self.well}")
        self.threedWin.move(510,110)
        self.ax3d.plot3D(self.wellDf['EW'], self.wellDf['NS'],self.wellDf['TVD'], label = 'Planned')
        self.ax3d.plot3D(self.wellA['EW'], self.wellA['NS'],self.wellA['TVD'], color = 'red', linestyle = 'dashed', label = 'Actual')
        self.ax3d.set_title(f"3D View - {self.well}")
        self.ax3d.set_xlabel('<-West - East->')
        self.ax3d.set_ylabel('<-North - South->')
        self.ax3d.grid(True)
        self.ax3d.invert_zaxis()
        self.ax3d.view_init(azim=225, elev=30)
        self.ax3d.set_zlabel('TVD [ft]')
        self.ax3d.tick_params(labelbottom=False, labelleft = False)
        self.ax3d.legend()
        self.threedWin.show()

    def formations(self):
        if self.ui.formationsBox.isChecked():
            if not self.formResults:
                QMessageBox.information(self, "No Formations Found", f"No formations were found for {self.well} in the database.\n"
                                        + "Please use the Formation Editor tool to enter some formations.")
                self.ui.formationsBox.setCheckState(Qt.CheckState.Unchecked)
            else:
                if self.sw:
                    for item in self.lines:
                        item.set_visible(True)
                    self.fig1.canvas.draw()
                if self.tw:
                    for item in self.lines1:
                        item.set_visible(True)
                        self.fig2.canvas.draw()
        else:
            if self.sw:
                for item in self.lines:
                    item.set_visible(False)
                self.fig1.canvas.draw()
            if self.tw:
                for item in self.lines1:
                    item.set_visible(False)
                    self.fig2.canvas.draw()
        return
    
    def closeEvent(self, event):
        self.updateP.close()
        self.updateA.close()
        self.sectionWin.close()
        self.planWin.close()
        self.tvdWin.close()
        self.threedWin.close()
        self.close()
        return 
>>>>>>> 9643a3c0a3ebc92bde83b6a0911e84090cacd830
