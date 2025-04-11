from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
import UI.selectionWindowUi as swUi
import existingWell as ew
import newWell as nw
import formations as form
import wellPath as wp
import wellBuilder as wb

class selectionWindow(QMainWindow):
    def __init__(self, well):
        super().__init__()
        self.well = well
        self.ui = swUi.Ui_selectionWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.move(50,50)
        self.ui.wellName.setText(self.well)
        self.show()
        
        self.ui.formationBtn.clicked.connect(self.formations)
        self.ui.wellPathBtn.clicked.connect(self.wellPath)
        self.ui.wellBuilderBtn.clicked.connect(self.wellBuild)
        self.ui.editWellBtn.clicked.connect(self.editWell)
        self.ui.changeWellBtn.clicked.connect(self.changeWell)
        
        
    def formations(self):
        self.form = form.formationsWindow(self.well)
        return

    def wellPath(self):
        self.wellPathWindow = wp.wellPath(self.well)
        return
    
    def editWell(self):
        self.edit = nw.newWell(self.well)
        self.hide()
        return
    
    def changeWell(self):
        self.change = ew.existingWell(self.well)
        self.hide()
        return

    def wellBuild(self):
        self.build = wb.wellBuilderWindow(self.well)
        return

    def closeEvent(self, event):
        quit = QMessageBox.critical(self, "Verify Close", "Are you sure you want to exit the program?", buttons=QMessageBox.Yes | QMessageBox.No)
        if quit == QMessageBox.No:
            event.ignore()
        else:
            QApplication.quit()
            return super().closeEvent(event)