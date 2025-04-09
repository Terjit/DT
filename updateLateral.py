import sqlite3
import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
import UI.addLatCsvUi as alUi

import lateralName as ln
import dirCalcs as dc


class updateLateral(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.ui = alUi.Ui_importLatCsvWin()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        pixmap = QPixmap('dev.png')
        self.ui.label_2.setPixmap(pixmap)

        self.addLatName = QMainWindow()

        self.ui.importBtn.clicked.connect(self.addLateral)
        self.ui.cancelBtn.clicked.connect(self.cancel)    

        self.show()
    
    def addLateral(self):
        self.hide()

        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", ".CSV Files (*.CSV)")
        if fileName:
            data = pd.read_csv(fileName)
            try:
                dataOut = dc.dirCalcs(data)
            except Exception as e:
                QMessageBox.critical(self, "Error With Directional Calculations", "Please verify your .csv is formated as shown and try again.")
                return
        dataOut['wellName'] = self.well
        dataOut['Planned'] = 1
        dataOut['Lateral'] = 'Null'

        self.addLatName = ln.updateLateral(self.well, dataOut)
        return

    def cancel(self):
        self.addLatName.close()
        self.close()
        return
    
    def closeEvent(self, event):
        self.addLatName.close()