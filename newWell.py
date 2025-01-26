import sqlite3
from math import floor
from PySide6.QtWidgets import QMainWindow, QMessageBox
import UI.newWellUi as nwUi
import drillingTools as dt
import selectionWindow as s

class newWell(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.ui = nwUi.Ui_newWell()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        
        self.ui.openBtn.clicked.connect(self.open)
        self.ui.cancelBtn.clicked.connect(self.cancel)
        self.ui.wellType.addItem('')
        self.ui.wellType.addItem('Producer')
        self.ui.wellType.addItem('Injector')
        self.ui.wellType.addItem('Exploration')
        
        if well != 'None':
            self.fill()        
        
        self.show()
        
    def fill(self):
        var = []
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM WELLS WHERE wellName = '{self.well}'")
        for item in data:
            for subItem in item:
                var.append(subItem)
        self.ui.operator.setText(var[0])
        self.ui.wellName.setText(var[2])
        self.ui.API.setText(var[1])
        self.ui.latDeg.setText(str(floor(float(var[3]))))
        self.ui.latMin.setText(str(floor(float(var[3])%1*60)))
        self.ui.latSec.setText(str(round(float(var[3])%1*60%1*60,4)))
        self.ui.lonDeg.setText(str(floor(float(var[4]))))
        self.ui.lonMin.setText(str(floor(float(var[4])%1*60)))
        self.ui.lonSec.setText(str(round(float(var[4])%1*60%1*60,4)))
        self.ui.wellType.setCurrentText(var[5])
        self.ui.openBtn.setText('Update Well')
        conn.close()
        return
        
    def open(self):
        #put all ip line edits in a list
        vars = []
        vars.append(self.ui.operator)
        vars.append(self.ui.API)
        vars.append(self.ui.wellName)
        vars.append(self.ui.latDeg)
        vars.append(self.ui.latMin)
        vars.append(self.ui.latSec)
        vars.append(self.ui.lonDeg)
        vars.append(self.ui.lonMin)
        vars.append(self.ui.lonSec)
        latDec = float(self.ui.latDeg.text())+float(self.ui.latMin.text())/60 + float(self.ui.latSec.text())/3600
        lonDec = float(self.ui.lonDeg.text())+float(self.ui.lonMin.text())/60 + float(self.ui.lonSec.text())/3600
        wellType = self.ui.wellType.currentText()
        api = vars[1].text()
        cleanAPI = api.replace('-','')
        
        #if updating well info
        if self.well != 'None':
            conn = sqlite3.connect('dt.db')
            cursor = conn.cursor()
            data = cursor.execute(f"SELECT rowid FROM WELLS WHERE wellName = '{self.well}'")
            for item in data:
                for subItem in item:
                    rowId = subItem
            data = cursor.execute("SELECT DISTINCT API from WELLS;")
            #Check that API is not already in database
            for item in data:
                for subItem in item:
                    if cleanAPI == subItem:
                        data1 = cursor.execute(f"SELECT DISTINCT wellName from WELLS where API = '{cleanAPI}';")
                        for item1 in data1:
                            for subItem1 in item1:
                                if subItem1 != self.well:
                                    QMessageBox.warning(self, 'Error', 'API # already exists in database.')
                                    self.ui.API.setStyleSheet("border: 1px solid red;")
                                    conn.close()
                                    return
            #check that API is correct length
            if len(cleanAPI) < 12:
                QMessageBox.warning(self, 'Error', 'Please verify API is at least 12 digits.')
                self.ui.API.setStyleSheet("border: 1px solid red;")
                conn.close()
                return
            cursor.execute(f"UPDATE WELLS SET operator = ?, API = ?, wellName = ?, latitude = ?, longitude = ?, wellType = ? WHERE rowid = {rowId}",
                           (vars[0].text(), cleanAPI, vars[2].text(), latDec, lonDec, wellType))
            conn.commit()
            conn.close()
            self.hide()
            self.selection = s.selectionWindow(vars[2].text())
            return             
        #check that all line edits (item) contain text     
        for item in vars:
            if item.text() == '':
                QMessageBox.warning(self, 'Missing Fields', 'Please make sure all fields are filled out.')
                for i in vars:
                    if i.text() == '':
                        i.setStyleSheet("border: 1px solid red;")
                    else:
                        i.setStyleSheet("border: none;")
                return
        #open connection to database, create cursor, pull all distinct wellNames from database         
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor() 
        data = cursor.execute("SELECT DISTINCT wellName from WELLS;")
        #check well name is not in the databse already
        for item in data:
            for subItem in item:
                if vars[2].text() == subItem:
                    QMessageBox.warning(self, 'Error', 'Well name already exists in database.')
                    self.ui.wellName.setStyleSheet("border: 1px solid red;")
                    conn.close()
                    return
        #pull all API numbers from database, obtain text from API line edit and remove -'s if entered
        data = cursor.execute("SELECT DISTINCT API from WELLS;")
        #Check that API is not already in database
        for item in data:
            for subItem in item:
                if cleanAPI == subItem:
                    QMessageBox.warning(self, 'Error', 'API # already exists in database.')
                    self.ui.API.setStyleSheet("border: 1px solid red;")
                    conn.close()
                    return
        #check that API is correct length
        if len(cleanAPI) < 12:
            QMessageBox.warning(self, 'Error', 'Please verify API is at least 12 digits.')
            self.ui.API.setStyleSheet("border: 1px solid red;")
            conn.close()
            return
        #check to see if a well type has been entered in the combo box
        if self.ui.wellType.currentText() == '':
            QMessageBox.warning(self, 'Error', 'Please select a well type.')
            self.ui.wellType.setStyleSheet("border: 1px solid red;")
            return
        #Convert latitude and longitude from deg min sec to decimal

        cursor.execute("INSERT INTO WELLS VALUES(?,?,?,?,?,?)", (vars[0].text(), cleanAPI, vars[2].text(), latDec, lonDec, wellType))
        conn.commit()
        conn.close()
        self.hide()
        self.selection = s.selectionWindow(vars[2].text())
          
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
