import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox
import UI.existingWellUi as ewUi
import drillingTools as dt
import selectionWindow as s

class existingWell(QMainWindow):
    def __init__(self, well = 'None'):
        super().__init__()
        self.ui = ewUi.Ui_openExistingWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.show()
        self.well = well
        self.dt = None
        self.wells = []
        self.operators = []
        self.blank = ''
        
        self.ui.operatorBox.addItem(self.blank)
        self.getOperators()

        self.ui.operatorBox.currentIndexChanged.connect(self.getWells)
        self.ui.openBtn.clicked.connect(self.open)
        self.ui.cancelBtn.clicked.connect(self.cancel)
   
    def getOperators(self):
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute("SELECT DISTINCT operator from WELLS;")
        for item in data:
            for subItem in item:
                self.ui.operatorBox.addItem(subItem)
        conn.close()    
        return    
    
    def getWells(self):
        self.ui.wellBox.clear()
        self.ui.wellBox.addItem(self.blank)
        value = self.ui.operatorBox.currentText()
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT DISTINCT wellName from WELLS WHERE operator = '{value}';")
        for item in data:
            for subItem in item:
                self.ui.wellBox.addItem(subItem)                  
        conn.close()   
        return
    
    def open(self):
        if self.ui.operatorBox.currentText() =='':
            QMessageBox.warning(self, "Missing Operator", "Please select an operator.")
        elif self.ui.wellBox.currentText() == '':
            QMessageBox.warning(self, "Missing Well", "Please select a well.")
        else:
            self.hide()
            well = self.ui.wellBox.currentText()
            self.selection = s.selectionWindow(well)
        
    def cancel(self):            
        self.hide()
        if self.well != 'None':
            self.main = s.selectionWindow(self.well)
            self.main.show()
        elif not self.dt:
            self.main = dt.dt()
            self.main.show()
    
    def closeEvent(self, event):
        if self.well != 'None':
            self.main = s.selectionWindow(self.well)
            self.main.show()
        else:
            quit = QMessageBox.critical(self, "Verify Close", "Are you sure you want to exit the program?", buttons=QMessageBox.Yes | QMessageBox.No)
            if quit == QMessageBox.No:
                event.ignore()
            else:
                return super().closeEvent(event)
