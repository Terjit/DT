from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd
import sqlite3
from matplotlib.backends.backend_pdf import PdfPages
import UI.outputDirReportUI as outUi



class outputDirPdf(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.well = well
        self.ui = outUi.Ui_MainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,355)

        self.ui.generateBtn.clicked.connect(self.generatePdf)

        self.show()

    def generatePdf(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", ".PDF Files (*.PDF)")

        conn = sqlite3.connect('dt.db')
        
        self.wellDf = pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{self.well}' AND Planned = 1 AND Lateral = 'NULL'", conn)
        self.wellDf = self.wellDf.drop(columns=['Planned','Lateral'])

        self.wellInfo = pd.read_sql_query(f"SELECT * FROM WELLS WHERE wellName = '{self.well}'", conn)
        
        self.figc = plt.Figure(figsize=(7.5,7.5))
        self.axc = self.figc.add_subplot()
        self.axc.axis('tight')
        self.axc.axis('off')
        self.axc.axis([0,10,0,10])
        self.axc.text(4,9, self.wellInfo['operator'].iloc[0] + " " + self.well, color='black', fontsize=12)
        self.axc.text(4,8.5, self.wellInfo['API'].iloc[0], color='black', fontsize=12)
        if self.ui.checkBox_2.isChecked():
            self.axc.text(4,7, "Plan - Section View", color='black', fontsize=12)
        if self.ui.checkBox_3.isChecked():
            self.axc.text(4,6.5, "Plan - TVD vs MD View", color='black', fontsize=12)
        if self.ui.checkBox_4.isChecked():
            self.axc.text(4,6, "Plan - Plan View", color='black', fontsize=12)
        if self.ui.checkBox_5.isChecked():
            self.axc.text(4,5.5, "Plan - Directional Data", color='black', fontsize=12)

        self.fig = plt.Figure(figsize=(12,7.5))
        self.ax = self.fig.add_subplot()
        self.ax.axis('tight')
        self.ax.axis('off')
        self.ax.table(cellText=self.wellDf.values,colLabels=self.wellDf.columns,loc='center')
        
        self.fig1 = plt.Figure(figsize=(7.5,7.5))
        self.axs = self.fig1.add_subplot()
        self.axs.plot(self.wellDf['NS'], self.wellDf['TVD'], color='black')
        self.axs.set_title("Section View TVD vs N/S")
        self.axs.set_xlabel('South(-) | North(+)')
        self.axs.set_ylabel('True Vertical Depth [ft]')
        self.axs.grid(True)
        self.axs.invert_yaxis()


        self.fig2 = plt.Figure(figsize=(7.5,7.5))
        self.ax2 = self.fig2.add_subplot()
        self.ax2.plot(self.wellDf['MD'], self.wellDf['TVD'], color='black')
        self.ax2.set_title("TVD vs MD")
        self.ax2.set_xlabel('Measure Depth [ft]')
        self.ax2.set_ylabel('True Vertical Depth [ft]')
        self.ax2.grid(True)
        self.ax2.invert_yaxis()

        self.figp = plt.Figure(figsize=(7.5,7.5))
        self.axp = self.figp.add_subplot()
        self.axp.plot(self.wellDf['EW'], self.wellDf['NS'], color='black')
        self.axp.set_title("N/S vs E/W")
        self.axp.set_xlabel('West(-) | East(+)')
        self.axp.set_ylabel('South(-) | North(+)')
        self.axp.grid(True)


        pp = PdfPages(fileName)
        if self.ui.checkBox.isChecked():
            pp.savefig(self.figc, bbox_inches='tight')
        if self.ui.checkBox_2.isChecked():
            pp.savefig(self.fig1, bbox_inches='tight')
        if self.ui.checkBox_3.isChecked():
            pp.savefig(self.fig2, bbox_inches='tight')
        if self.ui.checkBox_4.isChecked():
            pp.savefig(self.figp, bbox_inches='tight')
        if self.ui.checkBox_5.isChecked():
            pp.savefig(self.fig, bbox_inches='tight')
        pp.close()

        return