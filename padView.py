from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel, QCheckBox
import sqlite3
import UI.padViewUi as pvUi



class padView(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.pad = self.well.split('-')[0]
        self.showWell = []
        self.label = []
        self.highlight = []
        self.ui = pvUi.Ui_padView()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(250,355)
        
        conn = sqlite3.connect('dt.db')
        cursor = conn.cursor()
        
        data = cursor.execute(f"SELECT DISTINCT wellName FROM DEV WHERE wellName LIKE '{self.pad}%'")
        i = 0
        j = 0
        k = 0
        h = 41
        for item in data:
            for subItem in item:
                if h < 331:
                    h += 22
                self.showWell.append(QCheckBox())
                self.ui.gridLayout.addWidget(self.showWell[i], i+1, 0, 1, 1, alignment=Qt.AlignCenter)
                self.label.append(QLabel(f"{subItem}", self.ui.scrollAreaWidgetContents))
                self.ui.gridLayout.addWidget(self.label[j], j+1, 1, 1, 1, alignment=Qt.AlignCenter)
                self.highlight.append(QCheckBox())
                self.ui.gridLayout.addWidget(self.highlight[k], k+1, 2, 1, 1, alignment=Qt.AlignCenter)
                self.ui.scrollArea.setGeometry(QRect(10, 60, 173, h))
                self.showWell[i].stateChanged.connect(self.click)
                i += 1
                j += 1
                k += 1
        
           
            
        self.show()
        
    def click(self):
        print(True)
        return