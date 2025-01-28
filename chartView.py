from PySide6.QtWidgets import QMainWindow, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd
import sqlite3
import UI.chartViewUi as cvUi



class chartView(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.sw = False
        self.lines = []
        self.pullData()
        
        self.ui = cvUi.Ui_chartWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(250,355)
        
        self.ui.sectionBtn.clicked.connect(self.section)
        self.ui.planBtn.clicked.connect(self.plan)
        self.ui.threedBtn.clicked.connect(self.threed) 
        self.ui.formationsBox.stateChanged.connect(self.formations)

        self.show()

    def pullData(self):
        self.wellDf = pd.DataFrame()
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()        
        self.wellDf = pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{self.well}'", conn)
        self.formationData = cursor.execute(f"SELECT formationName, TVD FROM FORMATIONS WHERE wellName = '{self.well}' ORDER BY TVD ASC")
        self.formResults = self.formationData.fetchone()
        return
    
    def section(self):
        formations = []
        self.sectionWin = QMainWindow()
        self.figs = plt.Figure(figsize=(6.5,6.5))
        self.canvas = FigureCanvasQTAgg(self.figs)
        self.axs = self.figs.add_subplot()
        self.sectionWin.setCentralWidget(self.canvas)
        self.sectionWin.setWindowTitle(f"Section View - {self.well}")
        self.sectionWin.move(450,50)
        self.axs.plot(self.wellDf['NS'], self.wellDf['TVD'])
        self.axs.set_title("Section View TVD vs N/S")
        self.axs.set_xlabel('South(-) | North(+)')
        self.axs.set_ylabel('True Vertical Depth')
        self.axs.grid(True)
        self.axs.invert_yaxis()
        xmin, xmax = self.axs.get_xlim()
        self.axs.set_xlim(xmin, xmax)
        if self.formResults: 
            for item in self.formationData:
                formations.append(item)
            for item in formations:
                self.lines.append(self.axs.hlines(item[1], -100000, 100000, colors='green', linestyles='dashed', linewidth=0.75, visible=False))
                self.lines.append(self.axs.text(xmax, item[1], item[0], ha='right', va='bottom', fontsize=7.5, visible=False))
        self.sw = True
        self.sectionWin.show()
        return
    
    def plan(self):
        self.planWin = QMainWindow()
        self.figp = plt.Figure(figsize=(6.5,6.5))
        self.canvas = FigureCanvasQTAgg(self.figp)
        self.axp = self.figp.add_subplot()
        self.planWin.setCentralWidget(self.canvas)
        self.planWin.setWindowTitle(f"Plan View - {self.well}")
        self.planWin.move(470,70)
        self.axp.plot(self.wellDf['EW'], self.wellDf['NS'])
        self.axp.set_title("N/S vs E/W")
        self.axp.set_xlabel('West(-) | East(+)')
        self.axp.set_ylabel('South(-) | North(+)')
        self.axp.grid(True)
        self.planWin.show()
        return
    
    def threed(self):
        self.threedWin = QMainWindow()
        self.fig3d = plt.Figure(figsize=(6.5,6.5))
        self.canvas = FigureCanvasQTAgg(self.fig3d)
        self.ax3d = self.fig3d.add_subplot(projection="3d")
        self.threedWin.setCentralWidget(self.canvas)
        self.threedWin.setWindowTitle(f"3D View - {self.well}")
        self.threedWin.move(490,90)
        self.ax3d.plot3D(self.wellDf['EW'], self.wellDf['NS'],self.wellDf['TVD'])
        self.ax3d.set_title(f"3D View - {self.well}")
        self.ax3d.set_xlabel('<-West - East->')
        self.ax3d.set_ylabel('<-North - South->')
        self.ax3d.grid(True)
        self.ax3d.invert_zaxis()
        self.ax3d.view_init(azim=225, elev=30)
        self.ax3d.set_zlabel('TVD')
        self.ax3d.tick_params(labelbottom=False, labelleft = False)
        self.threedWin.show()
    
    def formations(self):
        if not self.sw:
            return
        elif self.ui.formationsBox.isChecked():
            if not self.formResults:
                QMessageBox.information(self, "No Formations Found", f"No formations were found for {self.well} in the database.\n"
                                        + "Please use the Formation Editor tool to enter some formations.")
            else:
                for item in self.lines:
                    item.set_visible(True)
                self.figs.canvas.draw()
        else:
            for item in self.lines:
                item.set_visible(False)
            self.figs.canvas.draw()
        return