from PySide6.QtWidgets import QApplication
import formations as f
import chartView as cv
import padView as pv
import wellPath as wp
import pva as pva
import updateDir as upDir




if __name__ == "__main__":
    app = QApplication()
    well = '3T-616'
    #win = cv.chartView(well)
    #win = pv.padView(well)
    #win = wp.wellPath(well)
    #win = pva.planVsActual(well)
    win = upDir.updateDir(well)

    app.exec()