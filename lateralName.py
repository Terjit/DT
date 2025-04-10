import sqlite3
import pandas as pd
from PySide6.QtCore import Qt, QRect, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
import UI.addLateralNameUi as alUi

class updateLateral(QMainWindow):
    def __init__(self, well='None', dataOut = 0):
        super().__init__()
        self.dt = None
        self.well = well
        self.dataOut = dataOut
        self.ui = alUi.Ui_updateLatNameWin()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())

        self.ui.addLateralBtn.clicked.connect(self.addLateral)
        self.ui.cancelBtn.clicked.connect(self.cancel)    
        self.ui.plannedBox.setCheckState(Qt.CheckState.Checked)
        self.ui.actualBox.clicked.connect(self.changeBoxA)
        self.ui.plannedBox.clicked.connect(self.changeBoxP)
        self.show()
    
    def addLateral(self):
        if self.ui.lineEdit.text() == '':
            QMessageBox.warning(self, "No Name Entered", "There was no name entered for the Lateral.")
            return
        
        if not self.ui.plannedBox.isChecked() and not self.ui.actualBox.isChecked():
            QMessageBox.warning(self, "Planned or Actual?", "Please select Planned or Actual.")
            return

        button = QMessageBox.question(self, "Confirm Update Lateral", "Updating the lateral well path will remove the current well path.\n"
                                        "Do you want to proceed?")
        if button == QMessageBox.No:
            self.close()
            return
        if self.ui.plannedBox.isChecked():
            self.planned = 1
        if self.ui.actualBox.isChecked():
            self.planned = 0
        self.lateral = self.ui.lineEdit.text()
        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM DEV WHERE wellName = ? AND Lateral = ?",(self.well, self.lateral))
        self.dataOut['Lateral'] = self.lateral 
        self.dataOut['Planned'] = self.planned
        for item in self.dataOut.iterrows():
            cursor.execute("INSERT INTO DEV VALUES(?,?,?,?,?,?,?,?,?,?)", 
                           (item[1].iloc[7],item[1].iloc[0],item[1].iloc[1],item[1].iloc[2],item[1].iloc[3],item[1].iloc[4],item[1].iloc[5],item[1].iloc[6],item[1].iloc[8],item[1].iloc[9]))

        conn.commit()
        conn.close()
        self.close()
        return

    def changeBoxA(self):
        if self.ui.actualBox.isChecked():
            self.ui.plannedBox.setCheckState(Qt.CheckState.Unchecked)
        return
    
    def changeBoxP(self):
        if self.ui.plannedBox.isChecked():
            self.ui.actualBox.setCheckState(Qt.CheckState.Unchecked)
        return

    def cancel(self):
        self.close()
        return