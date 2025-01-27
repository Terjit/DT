import sqlite3
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import Qt
import UI.formationsUi as formUi


class formationsWindow(QMainWindow):
    def __init__(self, well):
        super().__init__()
        self.well = well
        self.ui = formUi.Ui_formationWindow()
        self.ui.setupUi(self)
        self.vars = []
        self.setVars()
        self.y = 115
        self.inc = 0
        self.commit = True
        self.i = 0
        self.getFormations()
        self.resize(550,self.y)
        self.setFixedSize(550,self.y)
        self.setWindowTitle(f"Drilling Tools - Formation Editor - {self.well}")
        self.move(250,50)
        self.show()
        
        self.ui.addFormationBtn.clicked.connect(self.addFormation)
        self.ui.commitChangesBtn.clicked.connect(self.commitChanges)

    def commitChanges(self):
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        values = []
        count = 0
        cursor.execute(f"DELETE FROM FORMATIONS WHERE wellName = '{self.well}'")
        for item in self.vars:
            if item.text() != '':
                values.append(item.text())
        while count < 63:
                if self.vars[count].text() != '' or self.vars[count+1].text() != '' or self.vars[count+2].text() != '':
                    cursor.execute("INSERT INTO FORMATIONS VALUES(?,?,?,?)", (self.well, self.vars[count].text(), self.vars[count+1].text(), self.vars[count+2].text()))
                count += 3
        conn.commit()
        conn.close()
        self.commit = True
        self.close()
        return

    def getFormations(self):
        count = 0
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM FORMATIONS WHERE wellName = '{self.well}' ORDER BY MD ASC ")
        #if there are entries for the well in the database fill in the table with the values
        if data:
            for item in data:
                for subItem in item:
                    if count == 0:
                        count +=1
                    elif count %4 == 0:
                        self.inc += 1
                        if self.inc > 20:
                            QMessageBox.information(self, "Max Formations Reached", "You have reached the maximum allowed number of formations.")
                            return
                        self.y += 26
                        self.setFixedSize(550, self.y)
                        self.resize(550,self.y)
                        count +=1   
                    else:
                        self.vars[self.i].setText(str(subItem))
                        count += 1
                        self.i += 1
        conn.close()
     
    def addFormation(self):
        self.commit = False
        self.inc += 1
        if self.inc > 20:
            QMessageBox.information(self, "Max Formations Reached", "You have reached the maximum allowed number of formations.")
            return
        else:
            self.y += 26
            self.setFixedSize(550, self.y)
            self.resize(550,self.y)
       
    def setVars(self):
        self.vars.append(self.ui.f0)
        self.vars.append(self.ui.m0)
        self.vars.append(self.ui.t0)
        self.vars.append(self.ui.f1)
        self.vars.append(self.ui.m1)
        self.vars.append(self.ui.t1)
        self.vars.append(self.ui.f2)
        self.vars.append(self.ui.m2)
        self.vars.append(self.ui.t2)
        self.vars.append(self.ui.f3)
        self.vars.append(self.ui.m3)
        self.vars.append(self.ui.t3)
        self.vars.append(self.ui.f4)
        self.vars.append(self.ui.m4)
        self.vars.append(self.ui.t4)
        self.vars.append(self.ui.f5)
        self.vars.append(self.ui.m5)
        self.vars.append(self.ui.t5)
        self.vars.append(self.ui.f6)
        self.vars.append(self.ui.m6)
        self.vars.append(self.ui.t6)
        self.vars.append(self.ui.f7)
        self.vars.append(self.ui.m7)
        self.vars.append(self.ui.t7)
        self.vars.append(self.ui.f8)
        self.vars.append(self.ui.m8)
        self.vars.append(self.ui.t8)
        self.vars.append(self.ui.f9)
        self.vars.append(self.ui.m9)
        self.vars.append(self.ui.t9)
        self.vars.append(self.ui.f10)
        self.vars.append(self.ui.m10)
        self.vars.append(self.ui.t10)
        self.vars.append(self.ui.f11)
        self.vars.append(self.ui.m11)
        self.vars.append(self.ui.t11)
        self.vars.append(self.ui.f12)
        self.vars.append(self.ui.m12)
        self.vars.append(self.ui.t12)
        self.vars.append(self.ui.f13)
        self.vars.append(self.ui.m13)
        self.vars.append(self.ui.t13)
        self.vars.append(self.ui.f14)
        self.vars.append(self.ui.m14)
        self.vars.append(self.ui.t14)
        self.vars.append(self.ui.f15)
        self.vars.append(self.ui.m15)
        self.vars.append(self.ui.t15)
        self.vars.append(self.ui.f16)
        self.vars.append(self.ui.m16)
        self.vars.append(self.ui.t16)
        self.vars.append(self.ui.f17)
        self.vars.append(self.ui.m17)
        self.vars.append(self.ui.t17)
        self.vars.append(self.ui.f18)
        self.vars.append(self.ui.m18)
        self.vars.append(self.ui.t18)
        self.vars.append(self.ui.f19)
        self.vars.append(self.ui.m19)
        self.vars.append(self.ui.t19)
        self.vars.append(self.ui.f20)
        self.vars.append(self.ui.m20)
        self.vars.append(self.ui.t20)
        self.ui.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ui.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ui.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        return     

    def closeEvent(self, event):
        if not self.commit:
            quit = QMessageBox.critical(self, "Verify Close", "Are you sure you want to exit without commiting changes?", buttons=QMessageBox.Yes | QMessageBox.No)
            if quit == QMessageBox.No:
                event.ignore()
            else:
                return super().closeEvent(event)
