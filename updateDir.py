from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
import pandas as pd
import sqlite3
import dirCalcs as dc
import UI.updateDirUi as upDirUi
import updatePlanned as up
import updateActual as ua
import updateLateral as ul

class updateDir(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        
        self.ui = upDirUi.Ui_updateDirWin()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,355)
        self.updateP = QMainWindow()
        self.updateA = QMainWindow()
        self.updateL = QMainWindow()
        self.addLatName = QMainWindow()
        
        self.ui.updatePlanBtn.clicked.connect(self.plan)
        self.ui.updateActualBtn.clicked.connect(self.actual)
        self.ui.lateralBtn.clicked.connect(self.lateral)
        
        self.show()
    
    def plan(self):
        self.updateP = up.updatePlanned(self.well)
        return
    
    def actual(self):
        self.updateA = ua.updateActual(self.well)
        return
    
    def lateral(self):
        self.updateL = ul.updateLateral(self.well)
        return
    
    def closeEvent(self, event):
        self.updateP.close()
        self.updateA.close()
        self.updateL.close()
        
        return