from PySide6.QtWidgets import QApplication
import formations as f
import selectionWindow as s

if __name__ == "__main__":
    app = QApplication()
    well = '3T-612'
    win = s.selectionWindow(well)

    app.exec()