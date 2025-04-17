from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Slot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import UI.wellBuilderUi as wbUi
import addCasing as addC
import sqlite3


class wellBuilderWindow(QMainWindow):
    def __init__(self, well):
        super().__init__()
        self.well = well
        self.ui = wbUi.Ui_wellBuilder()
        self.wellSchWin = QMainWindow()
        self.addSurf = QMainWindow()
        self.ui.setupUi(self, well)
        self.setFixedSize(self.size())
        self.move(250,50)

        self.ui.surfaceBtn.clicked.connect(self.surface)
        self.ui.intBtn.clicked.connect(self.intermediate)
        self.wellSchematic()
        self.show()
    
    @Slot(str)
    def wellSchematic(self):
        self.fig = plt.Figure(figsize=(9,10))
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.axs = self.fig.add_subplot()
        self.wellSchWin.setCentralWidget(self.canvas)
        self.wellSchWin.setWindowTitle(f"Well Schematic - {self.well}")
        self.wellSchWin.move(450,50)
        self.axs.invert_yaxis()
        self.axs.axis('off')
        self.axs.set_xlim(-20,20)

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
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        data = cursor.execute(f"SELECT * FROM CASING WHERE wellName = '{self.well}'")
        for item in data:
            data1 = cursor1.execute(f"SELECT id FROM CSGDATA WHERE od = {item[3]} AND weight = '{item[4]}' AND grade = '{item[5]}'")
            for item1 in data1:
                self.id.append(item1[0])
            
            self.section.append(item[1])
            self.hole.append(item[2])
            self.od.append(item[3])
            self.top.append(item[6])
            self.bottom.append(item[7])
        conn.close()
        print(len(self.id))
        if len(self.id) > 0:
            self.axs.hlines(0, xmin=-25, xmax=-(self.hole[0]/2), color='green')
            self.axs.hlines(0, xmin=25, xmax=(self.hole[0]/2), color='green')
        else:
            self.axs.hlines(0, xmin=-25, xmax=-6, color='green')
            self.axs.hlines(0, xmin=25, xmax=6, color='green')
        i = 0
        while i < len(self.id):
            if self.section[i] == 'Surface':
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
            i += 1
        
        return
    
    def surface(self):
        self.addSurf = addC.addCasingWindow(self.well, 'Surface')
        self.addSurf.dataSignal.connect(self.wellSchematic)
        return

    def intermediate(self):
        self.addInt = addC.addCasingWindow(self.well, 'Intermediate')
        self.addInt.dataSignal.connect(self.wellSchematic)
        return


    def closeEvent(self, event):
        self.wellSchWin.close()
        self.addSurf.close()
        self.close()
        return