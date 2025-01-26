from PySide6.QtWidgets import QMainWindow, QMessageBox
import UI.chartViewUi as cvUi


class chartView(QMainWindow):
    def __init__(self, well='None'):
        super().__init__()
        self.dt = None
        self.well = well
        self.ui = cvUi.Ui_chartWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(250,355)
        
        self.ui.sectionBtn.clicked.connect(self.section)
        self.ui.planBtn.clicked.connect(self.plan)
        self.ui.threedBtn.clicked.connect(self.threed)    
        self.ui.formationsBox.checkStateChanged(self.formations)
        
        self.show()

    def pullData(self):
        pass
    
    def section(self):
        section = QMainWindow()
        
        pass
    
    def plan(self):
        pass
    
    def threed(self):
        pass
    
    def formations(self):
        pass