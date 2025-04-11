from PySide6.QtWidgets import QApplication
import selectionWindow as sw
import formations as f
import chartView as cv
import padView as pv
import wellPath as wp
import pva as pva
import updateDir as upDir
import outputDir as outDir
import wellBuilder as wb



if __name__ == "__main__":
    app = QApplication()
    well = '3T-616'
    
    #win = sw.selectionWindow(well)
    #win = wp.wellPath(well)
    #win = cv.chartView(well)
    #win = pv.padView(well)
    #win = pva.planVsActual(well)
    #win = upDir.updateDir(well)
    #win  = outDir.outputDirPdf(well)
    win = wb.wellBuilderWindow(well)
    
    app.exec()