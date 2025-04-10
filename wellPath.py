import sqlite3
from math import floor
from PySide6.QtWidgets import QMainWindow, QMessageBox
import UI.wellPathUi as wpUi
import importCsv as ic
import chartView as cv
import padView as pv
import pva as planV
import outputDir as outP
import updateDir as upDir

class wellPath(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.ui = wpUi.Ui_wellPathWindow()
        self.chartViewWindow = None
        self.padViewWindow = None
        self.planVactualWindow = None
        self.updateDirWindow = None
        self.outputPdfWindow = None
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,50)
        
        self.ui.chartBtn.clicked.connect(self.chartView)
        self.ui.padBtn.clicked.connect(self.padView)
        self.ui.planVactualBtn.clicked.connect(self.planVactual)
        self.ui.pdfBtn.clicked.connect(self.outputPdf)
        self.ui.updateBtn.clicked.connect(self.update)

        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        
        data = cursor.execute(f"SELECT * FROM DEV WHERE wellName = '{self.well}'")
        
        if data.fetchone():
            self.show()
        else:
            try:
                self.importCsv = ic.importCSV(self.well)
            except TypeError:
                self.show()
        conn.close()

    def chartView(self):
        self.chartViewWindow = cv.chartView(self.well)
        return
    
    def padView(self):
        self.padViewWindow = pv.padView(self.well)
        return

    def planVactual(self):
        self.planVactualWindow = planV.planVsActual(self.well)
        return

    def outputPdf(self):
        self.outputPdfWindow = outP.outputDirPdf(self.well)
        return

    def update(self):
        self.updateDirWindow = upDir.updateDir(self.well)
        return

    def closeEvent(self, event):
        if self.chartViewWindow is not None:
            self.chartViewWindow.close()
        if self.padViewWindow is not None:
            self.padViewWindow.close()
        if self.planVactualWindow is not None:
            self.planVactualWindow.close()
        if self.updateDirWindow is not None:
            self.updateDirWindow.close()
        if self.outputPdfWindow is not None:
            self.outputPdfWindow.close()
        self.close()
        return         

                    