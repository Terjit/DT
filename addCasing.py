from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
import UI.addCasingUi as addCsg
import sqlite3


class addCasingWindow(QMainWindow):
    def __init__(self, well):
        super().__init__()
        self.well = well
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

        self.show()

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
        self.od = float(self.ui.OdBox.currentText())
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f'SELECT DISTINCT weight FROM CSGDATA WHERE od = {self.od}')
        for item in data:
            for subItem in item:
                self.ui.weightBox.addItem(str(subItem))
        conn.close()
        return
    
    def fillBoxGrade(self):
        self.ui.gradeBox.clear()
        #try because when clearing the box it runs this function
        try:
            self.weight = float(self.ui.weightBox.currentText())
        except ValueError:
            pass
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f'SELECT DISTINCT grade FROM CSGDATA WHERE od = {self.od} and weight = {self.weight}')
        for item in data:
            for subItem in item:
                self.ui.gradeBox.addItem(str(subItem))
        conn.close()
        return
    
    def closeEvent(self, event):
        self.close()
        return