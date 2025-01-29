from PySide6.QtWidgets import QApplication
import formations as f
import chartView as cv
import padView as pv

if __name__ == "__main__":
    app = QApplication()
    well = '3S-714'
    #win = cv.chartView(well)
    win = pv.padView(well)

    app.exec()