from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Slot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import UI.wellBuilderUi as wbUi
import addCasing as addC
import removeCsg as rmvCsg
import sqlite3


class wellBuilderWindow(QMainWindow):
    def __init__(self, well):
        super().__init__()
        self.well = well
        self.flag = 0
        self.ui = wbUi.Ui_wellBuilder()
        self.wellSchWin = QMainWindow()
        self.addCond = QMainWindow()
        self.addSurf = QMainWindow()
        self.addInt = QMainWindow()
        self.addProd = QMainWindow()
        self.addLiner = QMainWindow()
        self.addTube = QMainWindow()
        self.rmvWin = QMainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,50)

        self.ui.condBtn.clicked.connect(self.cond)
        self.ui.surfaceBtn.clicked.connect(self.surface)
        self.ui.intBtn.clicked.connect(self.intermediate)
        self.ui.prodBtn.clicked.connect(self.prod)
        self.ui.lineBtn.clicked.connect(self.liner)
        self.ui.tubeBtn.clicked.connect(self.tube)
        self.ui.removeBtn.clicked.connect(self.remove)
        self.wellSchematic()
        self.show()
    
    @Slot(str)
    def wellSchematic(self):
        self.fig = plt.Figure(figsize=(9,10))
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.axs = self.fig.add_subplot()
        self.fig.tight_layout()
        self.wellSchWin.setCentralWidget(self.canvas)
        self.wellSchWin.setWindowTitle(f"Well Schematic - {self.well}")
        self.wellSchWin.move(450,50)
        self.axs.invert_yaxis()
        self.axs.axis('off')
        self.axs.set_xlim(-30,15)

        self.draw()

        self.wellSchWin.show()

        return
    
    def draw(self):
        self.section = []
        self.od = []
        self.id = []
        self.top = []
        self.bottom = []
        self.hole = []
        self.formName = []
        self.formDepth = []
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        data = cursor.execute(f"""SELECT * FROM CASING WHERE wellName = '{self.well}' ORDER BY CASE
                                WHEN sectionName = 'Conductor' THEN 1
                                WHEN sectionName = 'Surface' THEN 2
                                WHEN sectionName = 'Intermediate' THEN 3
                                WHEN sectionName = 'Liner' THEN 4
                                WHEN sectionName = 'Production' THEN 5
                                WHEN sectionName = 'Tubing' THEN 6
                              END""")
        i=0
        for item in data:
            data1 = cursor1.execute(f"SELECT id FROM CSGDATA WHERE od = {item[3]} AND weight = '{item[4]}' AND grade = '{item[5]}'")
            if data1.fetchone() is None:
                data1 = cursor1.execute(f"SELECT id FROM TUBDATA WHERE od = {item[3]} AND weight = '{item[4]}' AND grade = '{item[5]}'")
            else:
                data1 = cursor1.execute(f"SELECT id FROM CSGDATA WHERE od = {item[3]} AND weight = '{item[4]}' AND grade = '{item[5]}'")
            for item1 in data1:
                self.id.append(item1[0])
            
            self.section.append(item[1])
            self.hole.append(item[2])
            self.od.append(item[3])
            self.top.append(item[6])
            self.bottom.append(item[7])
            if item[1] == 'Intermediate':
                self.flag = i
            i += 1
        conn.close()
        if len(self.id) > 0:
            if self.section[0] == 'Conductor':
                self.axs.hlines(0, xmin=-30, xmax=-(self.id[0]/2), color='green')
                self.axs.hlines(0, xmin=25, xmax=(self.id[0]/2), color='green')
            else:
                self.axs.hlines(0, xmin=-30, xmax=-(self.hole[0]/2), color='green')
                self.axs.hlines(0, xmin=25, xmax=(self.hole[0]/2), color='green')
        else:
            self.axs.hlines(0, xmin=-30, xmax=-6, color='green')
            self.axs.hlines(0, xmin=25, xmax=6, color='green')
        i = 0
        while i < len(self.id):
            if self.section[i] == 'Conductor':
                self.axs.vlines((-self.id[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.vlines((self.id[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.hole[i] = self.id[i]
            elif self.section[i] == 'Surface' and i == 0:
                self.axs.vlines((-self.hole[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='brown')
                self.axs.vlines((self.hole[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='brown')
                self.axs.vlines((-self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.vlines((self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.hlines(self.bottom[i], self.od[i]/2, (self.od[i]/2+1), color='black')
                self.axs.hlines(self.bottom[i], -self.od[i]/2, -(self.od[i]/2+1), color='black')
                rightx = [(self.od[i]/2+1), (self.od[i]/2)]
                righty = [self.bottom[i],(self.bottom[i]-100)]
                leftx = [(-self.od[i]/2-1), (-self.od[i]/2)]
                lefty = [self.bottom[i],(self.bottom[i]-100)]
                self.axs.plot(rightx,righty, color='black')
                self.axs.plot(leftx,lefty, color='black')
            elif self.section[i] == 'Tubing':
                self.axs.vlines((-self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.vlines((self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
            else:
                self.axs.vlines((-self.hole[i]/2), ymin = self.bottom[i-1], ymax=self.bottom[i], color='brown')
                self.axs.vlines((self.hole[i]/2), ymin = self.bottom[i-1], ymax=self.bottom[i], color='brown')
                self.axs.vlines((-self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.vlines((self.od[i]/2), ymin = self.top[i], ymax=self.bottom[i], color='black')
                self.axs.hlines(self.bottom[i], self.od[i]/2, (self.od[i]/2+1), color='black')
                self.axs.hlines(self.bottom[i], -self.od[i]/2, -(self.od[i]/2+1), color='black')
                self.axs.hlines(self.bottom[i-1], self.hole[i]/2, (self.hole[i-1]/2), color='brown')
                self.axs.hlines(self.bottom[i-1], -self.hole[i]/2, -(self.hole[i-1]/2), color='brown')
                rightx = [(self.od[i]/2+1), (self.od[i]/2)]
                righty = [self.bottom[i],(self.bottom[i]-100)]
                leftx = [(-self.od[i]/2-1), (-self.od[i]/2)]
                lefty = [self.bottom[i],(self.bottom[i]-100)]
                self.axs.plot(rightx,righty, color='black')
                self.axs.plot(leftx,lefty, color='black')
            if self.section[i] == 'Liner' or self.section[i] == 'Production':
                self.axs.hlines(self.top[i], self.od[i]/2, (self.od[self.flag]/2), color='black')
                self.axs.hlines(self.top[i], -self.od[i]/2, -(self.od[self.flag]/2), color='black')
                self.axs.hlines(self.top[i]+250, self.od[i]/2, (self.od[self.flag]/2), color='black')
                self.axs.hlines(self.top[i]+250, -self.od[i]/2, -(self.od[self.flag]/2), color='black')
                rightx = [(self.od[i]/2), (self.od[self.flag]/2)]
                righty = [self.top[i],(self.top[i]+250)]
                rightx1 = [(self.od[self.flag]/2), (self.od[i]/2)]
                righty1 = [self.top[i],(self.top[i]+250)]
                leftx = [(-self.od[i]/2), (-self.od[self.flag]/2)]
                lefty = [self.top[i],(self.top[i]+250)]
                leftx1 = [(-self.od[self.flag]/2), (-self.od[i]/2)]
                lefty1 = [self.top[i],(self.top[i]+250)]
                self.axs.plot(rightx,righty, color='black')
                self.axs.plot(rightx1,righty1, color='black')
                self.axs.plot(leftx,lefty, color='black')
                self.axs.plot(leftx1,lefty1, color='black')
            elif self.section[i] == 'Tubing':
                self.axs.hlines(self.bottom[i]-250, self.od[i]/2, (self.od[self.flag]/2), color='black')
                self.axs.hlines(self.bottom[i]-250, -self.od[i]/2, -(self.od[self.flag]/2), color='black')
                self.axs.hlines(self.bottom[i]-500, self.od[i]/2, (self.od[self.flag]/2), color='black')
                self.axs.hlines(self.bottom[i]-500, -self.od[i]/2, -(self.od[self.flag]/2), color='black')
                rightx = [(self.od[i]/2), (self.od[self.flag]/2)]
                righty = [self.bottom[i]-250,(self.bottom[i]-500)]
                rightx1 = [(self.od[self.flag]/2), (self.od[i]/2)]
                righty1 = [self.bottom[i]-250,(self.bottom[i]-500)]
                leftx = [(-self.od[i]/2), (-self.od[self.flag]/2)]
                lefty = [self.bottom[i]-250,(self.bottom[i]-500)]
                leftx1 = [(-self.od[self.flag]/2), (-self.od[i]/2)]
                lefty1 = [self.bottom[i]-250,(self.bottom[i]-500)]
                self.axs.plot(rightx,righty, color='black')
                self.axs.plot(rightx1,righty1, color='black')
                self.axs.plot(leftx,lefty, color='black')
                self.axs.plot(leftx1,lefty1, color='black')
            i += 1
        #Pull formations and place on drawing
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM FORMATIONS WHERE wellName = '{self.well}'")
        if data.fetchone() is not None:
            i = 0
            for item in data:
                self.formName.append(item[1])
                self.formDepth.append(item[2])
                i += 1
            i=0
            while i < len(self.formName):
                try:
                    if self.formDepth[i] < max(self.bottom):
                        self.axs.hlines(self.formDepth[i], 7, 25, color='green', linestyles='dashed', linewidth=1)
                        self.axs.text(7,self.formDepth[i], self.formName[i], size=8)      
                    i += 1
                except ValueError:
                    i += 1
        conn.close()
        #Pull well info and place on drawing
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM WELLS WHERE wellName = '{self.well}'")
        for item in data:
            self.axs.text(-30,-50, item[0] + ' - ' + item[2] + ' - ' + item[1], size=15)
        conn.close()
        #Pull casing info and place on drawing
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = conn.execute(f"SELECT * FROM CASING WHERE wellName ='{self.well}'")
        for item in data:
            if item[1] == 'Conductor':
                self.axs.text(-30,item[7]+200,item[1] + ': ' + str(item[3]) + ' - ' + str(item[4]) + ' - ' + str(item[5]) + ": " + str(item[6]) + "-" + str(item[7]))
            elif item[1] == 'Tubing':
                self.axs.text(-30,item[7]*.90,item[1] + ': ' + str(item[3]) + ' - ' + str(item[4]) + ' - ' + str(item[5]) + ": " + str(item[6]) + " - " + str(item[7]))
            else:
                self.axs.text(-30,item[7],item[1] + ': ' + str(item[3]) + ' - ' + str(item[4]) + ' - ' + str(item[5]) + ": " + str(item[6]) + " - " + str(item[7]))
        conn.close()
        return
    
    def cond(self):
        self.addCond = addC.addCasingWindow(self.well, 'Conductor')
        self.addCond.dataSignal.connect(self.wellSchematic)
        return

    def surface(self):
        self.addSurf = addC.addCasingWindow(self.well, 'Surface')
        self.addSurf.dataSignal.connect(self.wellSchematic)
        return

    def intermediate(self):
        self.addInt = addC.addCasingWindow(self.well, 'Intermediate')
        self.addInt.dataSignal.connect(self.wellSchematic)
        return
    
    def prod(self):
        self.addProd = addC.addCasingWindow(self.well, 'Production')
        self.addProd.dataSignal.connect(self.wellSchematic)
        return
    
    def liner(self):
        self.addLiner = addC.addCasingWindow(self.well, 'Liner')
        self.addLiner.dataSignal.connect(self.wellSchematic)
        return

    def tube(self):
        self.addTube = addC.addCasingWindow(self.well, 'Tubing')
        self.addTube.dataSignal.connect(self.wellSchematic)
        return

    def remove(self):
        self.rmvWin = rmvCsg.removeCsgWin(self.well)
        self.rmvWin.dataSignal.connect(self.wellSchematic)
        return

    def closeEvent(self, event):
        self.wellSchWin.close()
        self.addSurf.close()
        self.addCond.close()
        self.addLiner.close()
        self.addInt.close()
        self.addProd.close()
        self.addTube.close()
        self.rmvWin.close()
        self.close()
        return