from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Signal
import UI.addCasingUi as addCsg
import sqlite3


class addCasingWindow(QMainWindow):

    dataSignal = Signal(str)

    def __init__(self, well, section='none'):
        super().__init__()
        self.well = well
        self.section = section
        self.blank = ''
        self.od = 0
        self.weight = 0
        self.ui = addCsg.Ui_addCasing()
        self.wellSchWin = QMainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.ui.OdBox.addItem(self.blank)
        
        self.fillBoxOd()

        self.ui.OdBox.currentIndexChanged.connect(self.fillBoxWeight)
        self.ui.weightBox.currentIndexChanged.connect(self.fillBoxGrade)
        self.ui.cancelBtn.clicked.connect(self.closeEvent)
        self.ui.submitBtn.clicked.connect(self.submit)

        self.show()
        return

    def fillBoxOd(self):
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute('SELECT DISTINCT od FROM CSGDATA')
        for item in data:
            for subItem in item:
                self.ui.OdBox.addItem(str(subItem))
        conn.close()
        return

    def fillBoxWeight(self):
        self.ui.weightBox.clear()
        try:
            self.od = float(self.ui.OdBox.currentText())
            conn = sqlite3.connect('dt.db')
            cursor = conn.cursor()
            data = cursor.execute(f'SELECT DISTINCT weight FROM CSGDATA WHERE od = {self.od}')
            for item in data:
                for subItem in item:
                    self.ui.weightBox.addItem(str(subItem))
            conn.close()
        except ValueError:
            self.ui.weightBox.clear()
        return
    
    def fillBoxGrade(self):
        self.ui.gradeBox.clear()
        #try because when clearing the box it runs this function
        try:
            self.weight = float(self.ui.weightBox.currentText())
            conn = sqlite3.connect('dt.db')
            cursor = conn.cursor()
            data = cursor.execute(f'SELECT DISTINCT grade FROM CSGDATA WHERE od = {self.od} and weight = {self.weight}')
            for item in data:
                for subItem in item:
                    self.ui.gradeBox.addItem(str(subItem))
            conn.close()
        except ValueError:
            self.ui.weightBox.clear()
            pass

        return
    
    def submit(self):
        try:
            self.holeDia = float(self.ui.holeDia.text())
            self.od = float(self.ui.OdBox.currentText())
            self.weight = float(self.ui.weightBox.currentText())
            self.grade = self.ui.gradeBox.currentText()
            self.top = float(self.ui.casingTop.text())
            self.bottom = float(self.ui.casingBottom.text())
            conn = sqlite3.connect('dt.db')
            cursor = conn.cursor()
            data = cursor.execute(f"SELECT * FROM CASING WHERE wellName = '{self.well}' AND sectionName = '{self.section}'")
            if data.fetchone is not None:
                button = QMessageBox.question(self, "Casing Already Exists", f"The {self.section} casing already exists in the database. Do you want to overwrite?")
                if button == QMessageBox.Yes:
                    cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' and sectionName = '{self.section}'")
                    cursor.execute("INSERT INTO CASING VALUES(?,?,?,?,?,?,?,?)", 
                            (self.well, self.section, self.holeDia, self.od, self.weight, self.grade, self.top, self.bottom))
                else:
                    self.close()
                    return
            else:
                cursor.execute("INSERT INTO CASING VALUES(?,?,?,?,?,?,?)", 
                            (self.well, self.section, self.od, self.weight, self.grade, self.top, self.bottom))
            conn.commit()
            self.dataSignal.emit(self.well)
            self.close()
        except ValueError:
            QMessageBox.critical(self, "Missing Values", "All Boxes need to contain a value. Please check and Submit again.")
            try:
                float(self.ui.holeDia.text())
                self.ui.holeDia.setStyleSheet("border: 1px solid gray;")
            except ValueError:
                self.ui.holeDia.setStyleSheet("border: 1px solid red;")
            try:
                float(self.ui.OdBox.currentText())
                self.ui.OdBox.setStyleSheet("border: 1px solid gray;")
                self.ui.weightBox.setStyleSheet("border: 1px solid gray;")
                self.ui.gradeBox.setStyleSheet("border: 1px solid gray;")
            except ValueError:
                self.ui.OdBox.setStyleSheet("border: 1px solid red;")
                self.ui.weightBox.setStyleSheet("border: 1px solid red;")
                self.ui.gradeBox.setStyleSheet("border: 1px solid red;")
            try:
                float(self.ui.casingTop.text())
                self.ui.casingTop.setStyleSheet("border: 1px solid gray;")
            except ValueError:
                self.ui.casingTop.setStyleSheet("border: 1px solid red;")
            try:
                float(self.ui.casingBottom.text())
                self.ui.casingBottom.setStyleSheet("border: 1px solid gray;")
            except ValueError:
                self.ui.casingBottom.setStyleSheet("border: 1px solid red;")
        
        return

    def closeEvent(self, event):
        self.close()
        return