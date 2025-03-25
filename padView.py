from PySide6.QtCore import Qt, QRect, Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel, QCheckBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import sqlite3
import pandas as pd
import dirCalcs as dc
import addWell as aw
import UI.padViewUi as pvUi

class padView(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.pad = self.well.split('-')[0]
        self.showWell = []
        self.showWellA = []
        self.label = []
        self.labelA = []
        self.highlight = []
        self.highlightA = []
        self.annotate = []
        self.annotateA = []
        self.annotateFlat = []
        self.annotateFlatA = []
        self.ui = pvUi.Ui_padView()
        self.threedWin = QMainWindow()
        self.flatWin = QMainWindow()
        self.addWellWin = QMainWindow()
        self.ui.setupUi(self, self.pad)
        self.setFixedSize(self.size())
        self.move(250,355)
        self.getWells()
        self.generateBoxes()
        self.padThreed()
        self.show()

        self.ui.annotationsBox.clicked.connect(self.annotateCheck)
        self.ui.addWellBtn.clicked.connect(self.addWellWindow)
        return

    def getWells(self):
        self.wellDf = pd.DataFrame()
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        wells = []
        wellsA = []
        gobodygook = []
        self.wellsP = []
        self.wellsDf = []
        dataP = []
        data = cursor.execute(f"SELECT wellName FROM WELLS WHERE wellName like '{self.pad}%' ORDER BY wellName ASC")
        for item in data:
            for subItem in item:
                wells.append(subItem)

        data = cursor.execute(f"SELECT DISTINCT wellName from DEV WHERE Planned = 0")
        for item in data:
            for subItem in item:
                gobodygook.append(subItem)
        for item in wells:
            if item in gobodygook:
                self.wellsDf.append(pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{item}' AND Planned = 0", conn))

        j = 0
        dataA = cursor.execute(f"SELECT DISTINCT wellName FROM DEV where Planned = 0")
        for item in dataA:
            for subItem in item:
                wellsA.append(subItem)
                data = cursor.execute(f"SELECT latitude, longitude FROM WELLS WHERE wellName = '{subItem}'")
                for item in data:
                    lat, lon = item
                x, y = dc.latLon(lat, lon)
                try:
                    self.wellsDf[j]['EW'] += x
                except IndexError:
                    pass
                try:
                    self.wellsDf[j]['NS'] += y
                except IndexError:
                    pass
            j += 1

        for item in wells:
            if item not in wellsA:
                self.wellsP.append(pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{item}'", conn))
                dataP.append(item)
        
        j = 0
        for item in dataP:
            data = cursor.execute(f"SELECT latitude, longitude FROM WELLS WHERE wellName = '{item}'")
            for item1 in data:
                lat, lon = item1
            x, y = dc.latLon(lat, lon)
            self.wellsP[j]['EW'] += x
            self.wellsP[j]['EW'].fillna(x)
            self.wellsP[j]['NS'] += y
            self.wellsP[j]['NS'].fillna(y)
            j += 1  
        conn.close()
        return

    def generateBoxes(self):        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        data = cursor.execute(f"SELECT DISTINCT wellName FROM DEV WHERE wellName LIKE '{self.pad}%' ORDER BY wellName ASC")
        i = 0
        iA = 0
        iT = 0
        j = 0
        jA = 0
        jT = 0
        k = 0
        kA = 0
        kT = 0
        h = 41
        for item in data:
            for subItem in item:
                if h < 331:
                    h += 22
                data1 = cursor1.execute(f"SELECT * FROM DEV WHERE wellName = '{subItem}' AND Planned = 0")
                if data1.fetchone() is not None:
                    self.showWellA.append(QCheckBox())
                    self.ui.gridLayout.addWidget(self.showWellA[iA], iT+1, 0, 1, 1, alignment=Qt.AlignCenter)
                    self.showWellA[iA].setCheckState(Qt.CheckState.Checked)
                    self.labelA.append(QLabel(f"{subItem}", self.ui.scrollAreaWidgetContents))
                    self.ui.gridLayout.addWidget(self.labelA[jA], jT+1, 1, 1, 1, alignment=Qt.AlignCenter)
                    self.highlightA.append(QCheckBox())
                    self.ui.gridLayout.addWidget(self.highlightA[kA], kT+1, 2, 1, 1, alignment=Qt.AlignCenter)
                    self.ui.scrollArea.setGeometry(QRect(10, 80, 173, h))
                    if self.labelA[jA].text() == self.well:
                        self.highlightA[kA].setCheckState(Qt.CheckState.Checked)
                    self.showWellA[iA].stateChanged.connect(self.padThreed)
                    self.highlightA[kA].stateChanged.connect(self.padThreed)
                    iA += 1
                    jA += 1
                    kA += 1
                    self.annotateA.append(1)
                    self.annotateFlatA.append(1)
                else:
                    self.showWell.append(QCheckBox())
                    self.ui.gridLayout.addWidget(self.showWell[i], iT+1, 0, 1, 1, alignment=Qt.AlignCenter)
                    self.showWell[i].setCheckState(Qt.CheckState.Checked)
                    self.label.append(QLabel(f"{subItem}", self.ui.scrollAreaWidgetContents))
                    self.ui.gridLayout.addWidget(self.label[j], jT+1, 1, 1, 1, alignment=Qt.AlignCenter)
                    self.highlight.append(QCheckBox())
                    self.ui.gridLayout.addWidget(self.highlight[k], kT+1, 2, 1, 1, alignment=Qt.AlignCenter)
                    self.ui.scrollArea.setGeometry(QRect(10, 80, 173, h))
                    if self.label[j].text() == self.well:
                        self.highlight[k].setCheckState(Qt.CheckState.Checked)
                    self.showWell[i].stateChanged.connect(self.padThreed)
                    self.highlight[k].stateChanged.connect(self.padThreed)
                    i += 1
                    j += 1
                    k += 1
                    self.annotate.append(1)
                    self.annotateFlat.append(1)
                iT += 1
                jT += 1
                kT += 1
        return
    
    def showCheck(self):
        j = 0
        for item in self.showWellA:
            if item.isChecked():
                try:
                    self.ax3d.plot3D(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'],self.wellsDf[j]['TVD'], color='black')
                    self.axFlat.plot(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'], color='black')
                except IndexError:
                    pass
            j += 1
        j = 0
        for item in self.showWell:
            if item.isChecked():
                try:
                    self.ax3d.plot3D(self.wellsP[j]['EW'], self.wellsP[j]['NS'],self.wellsP[j]['TVD'], color='black', linestyle='dashed')
                    self.axFlat.plot(self.wellsP[j]['EW'], self.wellsP[j]['NS'], color='black', linestyle='dashed')
                except IndexError:
                    pass
            j += 1
        return
    
    def highlightCheck(self):
        j = 0
        for item in self.highlightA:
            if item.isChecked() and self.showWellA[j].isChecked():
                try:
                    self.ax3d.plot3D(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'],self.wellsDf[j]['TVD'], color='red')
                    self.axFlat.plot(self.wellsDf[j]['EW'], self.wellsDf[j]['NS'], color='red')
                except IndexError:
                    pass
            else:
                item.setCheckState(Qt.CheckState.Unchecked)
            j += 1
        j = 0
        for item in self.highlight:
            if item.isChecked() and self.showWell[j].isChecked():
                try:
                    self.ax3d.plot3D(self.wellsP[j]['EW'], self.wellsP[j]['NS'],self.wellsP[j]['TVD'], color='red', linestyle='dashed')
                    self.axFlat.plot(self.wellsP[j]['EW'], self.wellsP[j]['NS'], color='red', linestyle='dashed')
                except IndexError:
                    pass
            else:
                item.setCheckState(Qt.CheckState.Unchecked)
            j += 1
        return

    def annotateCheck(self):
        if self.ui.annotationsBox.isChecked():
            j=0
            for item in self.showWellA:
                if item.isChecked():
                    try:
                        self.annotateA[j].set_visible(True)
                        self.annotateFlatA[j].set_visible(True)
                    except (AttributeError, IndexError):
                        pass
                j += 1
            j=0
            for item in self.showWell:
                if item.isChecked():
                    try:
                        self.annotate[j].set_visible(True)
                        self.annotateFlat[j].set_visible(True)
                    except (AttributeError, IndexError):
                        pass
                j += 1
            self.canvas.draw()
            self.canvasFlat.draw()
        else:
            for item in self.annotate:
                try:
                    item.set_visible(False)
                except (AttributeError, IndexError):
                    pass
            for item in self.annotateA:
                try:
                    item.set_visible(False)
                except (AttributeError, IndexError):
                    pass
            for item in self.annotateFlatA:
                try:
                    item.set_visible(False)
                except (AttributeError, IndexError):
                    pass
            for item in self.annotateFlat:
                try:
                    item.set_visible(False)
                except (AttributeError, IndexError):
                    pass
            self.canvas.draw()
            self.canvasFlat.draw()
        return

    def padThreed(self):
        self.fig3d = plt.Figure(figsize=(7.5,7.5))
        self.canvas = FigureCanvasQTAgg(self.fig3d)
        self.ax3d = self.fig3d.add_subplot(projection="3d")
        self.threedWin.setCentralWidget(self.canvas)
        self.threedWin.setWindowTitle(f"3D View - {self.pad}")
        self.threedWin.move(450,50)
        self.ax3d.set_title(f"3D View - {self.pad} pad")
        self.ax3d.set_xlabel('<-West - East->')
        self.ax3d.set_ylabel('<-North - South->')
        self.ax3d.grid(True)
        self.ax3d.invert_zaxis()
        self.ax3d.view_init(azim=225, elev=30)
        self.ax3d.set_zlabel('TVD')
        self.ax3d.tick_params(labelbottom=False, labelleft = False)
        j = 0
        for _ in self.labelA:
            try:
                self.annotateA[j] = self.ax3d.text(self.wellsDf[j]['EW'].iloc[-1], self.wellsDf[j]['NS'].iloc[-1], self.wellsDf[j]['TVD'].iloc[-1], self.labelA[j].text())
                self.annotateA[j].set_visible(False)
            except IndexError as e:
                pass
            j += 1
        j = 0
        for _ in self.label:
            try:
                self.annotate[j] = self.ax3d.text(self.wellsP[j]['EW'].iloc[-1], self.wellsP[j]['NS'].iloc[-1], self.wellsP[j]['TVD'].iloc[-1], self.label[j].text())
                self.annotate[j].set_visible(False)
            except IndexError as e:
                pass    
            j += 1

        self.padFlat()
        self.showCheck()
        self.highlightCheck()
        self.annotateCheck()
        self.threedWin.show()
        self.flatWin.show()
        return

    def padFlat(self):
        self.flat = plt.Figure(figsize=(7.5,7.5))
        self.canvasFlat = FigureCanvasQTAgg(self.flat)
        self.axFlat = self.flat.add_subplot()
        self.flatWin.setCentralWidget(self.canvasFlat)
        self.flatWin.setWindowTitle(f"Plan View - {self.pad}")
        self.flatWin.move(1210,50)
        self.axFlat.set_title(f"Plan View - {self.pad} pad")
        self.axFlat.set_xlabel('<-West - East->')
        self.axFlat.set_ylabel('<-North - South->')
        self.axFlat.grid(True)
        self.axFlat.tick_params(labelbottom=False, labelleft = False)
        j = 0
        for _ in self.labelA:
            try:
                self.annotateFlatA[j] = self.axFlat.text(self.wellsDf[j]['EW'].iloc[-1], self.wellsDf[j]['NS'].iloc[-1], self.labelA[j].text())
                self.annotateFlatA[j].set_visible(False)
            except IndexError as e:
                pass
            j += 1
        j = 0
        for _ in self.label:
            try:
                self.annotateFlat[j] = self.axFlat.text(self.wellsP[j]['EW'].iloc[-1], self.wellsP[j]['NS'].iloc[-1], self.label[j].text())
                self.annotateFlat[j].set_visible(False)
            except IndexError:
                pass    
            j += 1

        return

    def addWellWindow(self):
        self.addWellWin = aw.addWell(self.pad)
        self.addWellWin.dataSignal.connect(self.addWell)
        return

    @Slot(str)
    def addWell(self, well):
        #query DB for wellname and Planned = 0 if it is then add to showWellP and highlightP
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT * FROM DEV WHERE wellName = '{well}' and Planned = 0")
        if data.fetchone() is not None:
            i = len(self.showWellA)
            spot = len(self.showWell) + len(self.showWellA)
            self.showWellA.append(QCheckBox())
            self.ui.gridLayout.addWidget(self.showWellA[i], spot+1, 0, 1, 1, alignment=Qt.AlignCenter)
            self.labelA.append(QLabel(f"{well}", self.ui.scrollAreaWidgetContents))
            self.ui.gridLayout.addWidget(self.labelA[i], spot+1, 1, 1, 1, alignment=Qt.AlignCenter)
            self.highlightA.append(QCheckBox())
            self.ui.gridLayout.addWidget(self.highlightA[i], spot+1, 2, 1, 1, alignment=Qt.AlignCenter)
            self.showWellA[i].stateChanged.connect(self.padThreed)
            self.highlightA[i].stateChanged.connect(self.padThreed)
            h = 22*(spot+1) + 41
            if h < 331:
                self.ui.scrollArea.setGeometry(QRect(10, 80, 173, h))
        else:
            i = len(self.showWell)
            spot = len(self.showWell) + len(self.showWellA)
            self.showWell.append(QCheckBox())
            self.ui.gridLayout.addWidget(self.showWell[i], spot+1, 0, 1, 1, alignment=Qt.AlignCenter)
            self.label.append(QLabel(f"{well}", self.ui.scrollAreaWidgetContents))
            self.ui.gridLayout.addWidget(self.label[i], spot+1, 1, 1, 1, alignment=Qt.AlignCenter)
            self.highlight.append(QCheckBox())
            self.ui.gridLayout.addWidget(self.highlight[i], spot+1, 2, 1, 1, alignment=Qt.AlignCenter)
            self.showWell[i].stateChanged.connect(self.padThreed)
            self.highlight[i].stateChanged.connect(self.padThreed)
            h = 22*(spot+1) + 41
            if h < 331:
                self.ui.scrollArea.setGeometry(QRect(10, 80, 173, h))

        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        test = cursor.execute(f"SELECT * FROM DEV WHERE wellName = '{well}' AND Planned = 0")
        if test.fetchone() != None:
            self.wellsDf.append(pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{well}' AND Planned = 0", conn))
            data = cursor.execute(f"SELECT latitude, longitude FROM WELLS WHERE wellName = '{well}'")
            for item in data:
                lat, lon = item
            x, y = dc.latLon(lat, lon)
            self.wellsDf[-1]['EW'] += x
            self.wellsDf[-1]['NS'] += y
        else:
            self.wellsP.append(pd.read_sql_query(f"SELECT * FROM DEV WHERE wellName = '{well}' AND Planned = 1", conn))
            data = cursor.execute(f"SELECT latitude, longitude FROM WELLS WHERE wellName = '{well}'")
            for item in data:
                lat, lon = item
            x, y = dc.latLon(lat, lon)
            self.wellsDf[-1]['EW'] += x
            self.wellsDf[-1]['NS'] += y
        try:
            i = len(self.showWellA) - 1
            self.annotateA.append(self.ax3d.text(self.wellsDf[i]['EW'].iloc[-1], self.wellsDf[i]['NS'].iloc[-1], self.wellsDf[i]['TVD'].iloc[-1], self.labelA[i].text()))
            self.annotateFlatA.append(self.axFlat.text(self.wellsDf[i]['EW'].iloc[-1], self.wellsDf[i]['NS'].iloc[-1], self.labelA[i].text()))
        except IndexError:
            pass
        try:
            i = len(self.showWell) - 1
            self.annotate.append(self.ax3d.text(self.wellsP[i]['EW'].iloc[-1], self.wellsP[i]['NS'].iloc[-1], self.wellsP[i]['TVD'].iloc[-1], self.label[i].text()))
            self.annotateFlat.append(self.axFlat.text(self.wellsDf[i]['EW'].iloc[-1], self.wellsDf[i]['NS'].iloc[-1], self.labelA[i].text()))
        except IndexError:
            pass
        conn.close()

        return

    def closeEvent(self, event):
        self.threedWin.close()
        self.flatWin.close()
        self.addWellWin.close()
        self.close()
        return
