import UI.dtUi as dtUi
from PySide6.QtWidgets import QMainWindow, QMessageBox
import existingWell as ew
import newWell as nw

class dt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = dtUi.Ui_newWell()
        self.ui.setupUi(self)
        self.ui.openWell.clicked.connect(self.openWellUi)
        self.ui.createWell.clicked.connect(self.createWellUi)
        self.setFixedSize(self.size())
        self.show()

    def openWellUi(self):
        self.open = ew.existingWell()
        self.hide()
    
    def createWellUi(self):
        self.new = nw.newWell()
        self.hide()

    def closeEvent(self, event):
        quit = QMessageBox.critical(self, "Verify Close", "Are you sure you want to exit the program?", buttons=QMessageBox.Yes | QMessageBox.No)
        if quit == QMessageBox.No:
            event.ignore()
        else:
            return super().closeEvent(event)