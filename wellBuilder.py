from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import UI.wellBuilderUi as wbUi
import addCasing as addC


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
        self.wellSchematic()

        self.ui.surfaceBtn.clicked.connect(self.surface)

        self.show()


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
        self.axs.hlines(0, xmin=-25, xmax=-6, color='green')
        self.axs.hlines(0, xmin=25, xmax=6, color='green')
        self.wellSchWin.show()

        return

    def surface(self):
        self.addSurf = addC.addCasingWindow(self.well, 'surface')
        return



    def closeEvent(self, event):
        self.wellSchWin.close()
        self.addSurf.close()
        self.close()
        return