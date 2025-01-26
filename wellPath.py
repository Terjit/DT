import sqlite3
from math import floor
from PySide6.QtWidgets import QMainWindow, QMessageBox
import UI.wellPathUi as wpUi
import importCsv as ic
import chartView as cv

class wellPath(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.ui = wpUi.Ui_wellPathWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(250,50)
        
        self.ui.chartBtn.clicked.connect(self.chartView)
        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        
        data = cursor.execute(f"SELECT * FROM DEV WHERE wellName = '{self.well}'")
        
        if data.fetchone():
            self.show()
        else:
            try:
                self.importCsv = ic.importCSV(self.well)
            except TypeError:
                print(True)
                self.show()

    def chartView(self):
        self.chartViewWindow = cv.chartView()
        
        

                    