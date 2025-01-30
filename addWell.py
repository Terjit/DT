import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Signal
import UI.addWellUi as awUi
import padView as pv

class addWell(QMainWindow):

    dataSignal = Signal(str)

    def __init__(self, pad='None'):
        super().__init__()
        self.dt = None
        self.pad = pad
        self.ui = awUi.Ui_addWell()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.wells = []
        self.getWells()
        self.ui.addWellBtn.clicked.connect(self.openWell)
        self.ui.cancelBtn.clicked.connect(self.cancel)

        self.show()
    
    def getWells(self):
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()

        data = cursor.execute(f"SELECT wellName FROM WELLS WHERE wellName NOT LIKE '{self.pad}%'")

        for item in data:
            for subItem in item:
                self.wells.append(subItem)
        
        for item in self.wells:
            self.ui.comboBox.addItem('')
            self.ui.comboBox.addItem(item)
        
        conn.close()
        return
    
    def openWell(self):
        well = self.ui.comboBox.currentText()
        self.dataSignal.emit(well)
        self.close()

    def cancel(self):
        self.close()