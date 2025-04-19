from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Signal
import UI.removeCsgUi as rmvCsg
import sqlite3


class removeCsgWin(QMainWindow):

    dataSignal = Signal(str)

    def __init__(self, well, section='none'):
        super().__init__()
        self.well = well
        self.section = []
        self.blank = ''
        self.ui = rmvCsg.Ui_removeCsg()

        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.ui.checkBox.hide()
        self.ui.checkBox_2.hide()
        self.ui.checkBox_3.hide()
        self.ui.checkBox_4.hide()
        self.ui.checkBox_5.hide()
        self.ui.checkBox_6.hide()
        self.showBoxes()
        self.ui.removeBtn.clicked.connect(self.remove)
        self.ui.cancelBtn.clicked.connect(self.closeEvent)

        self.show()
        return
    
    def showBoxes(self):
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM CASING WHERE wellName = '{self.well}'")
        for item in data:
            if item[1] == 'Conductor':
                self.ui.checkBox.show()
                self.section.append(item[1])
            elif item[1] == 'Surface':
                self.ui.checkBox_2.show()
                self.section.append(item[1])
            elif item[1] == 'Intermediate':
                self.ui.checkBox_3.show()
                self.section.append(item[1])
            elif item[1] == 'Liner':
                self.ui.checkBox_4.show()
                self.section.append(item[1])
            elif item[1] == 'Production':
                self.ui.checkBox_5.show()
                self.section.append(item[1])
            elif item[1] == 'Tubing':
                self.ui.checkBox_6.show()
                self.section.append(item[1])
        conn.close()
        return

    def remove(self):
        button = QMessageBox.question(self, "Confirm Remove Casing", f"Please confirm removing casing string.")
        if button == QMessageBox.Yes:
            conn = sqlite3.connect('dt.db')
            cursor = conn.cursor()
            if self.ui.checkBox.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Conductor'")
            if self.ui.checkBox_2.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Surface'")
            if self.ui.checkBox_3.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Intermediate'")
            if self.ui.checkBox_4.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Liner'")
            if self.ui.checkBox_5.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Production'")
            if self.ui.checkBox_6.isChecked():
                cursor.execute(f"DELETE FROM CASING WHERE wellName = '{self.well}' AND sectionName = 'Tubing'")
            conn.commit()
            conn.close()
        self.dataSignal.emit(self.well)
        self.close()
        return

    def closeEvent(self, event):
        self.close()
        return