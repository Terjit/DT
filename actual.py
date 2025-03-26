from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
import pandas as pd
import sqlite3
import dirCalcs as dc
import UI.importCsvUi as acUi

class updateActual(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        
        self.ui = acUi.Ui_importCsvWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        pixmap = QPixmap('dev.png')
        self.ui.label_2.setPixmap(pixmap)
        
        self.ui.cancelBtn.clicked.connect(self.cancel)
        self.ui.importBtn.clicked.connect(self.importCsv)        
        
        self.show()
        
    def importCsv(self):
        
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", ".CSV Files (*.CSV)")
        if fileName:
            data = pd.read_csv(fileName)
            try:
                dataOut = dc.dirCalcs(data)
            except Exception as e:
                QMessageBox.critical(self, "Error With Directional Calculations", "Please verify your .csv is formated as shown and try again.")
                return
        dataOut['wellName'] = self.well
        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        for item in dataOut.iterrows():
            cursor.execute("INSERT INTO DEV VALUES(?,?,?,?,?,?,?,?)", 
                           (item[1].iloc[7],item[1].iloc[0],item[1].iloc[1],item[1].iloc[2],item[1].iloc[3],item[1].iloc[4],item[1].iloc[5],item[1].iloc[6]))
            
        conn.commit()
        conn.close()
        self.close()
        return
        
    def cancel(self):
        self.close()