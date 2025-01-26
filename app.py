from PySide6.QtWidgets import QApplication
import drillingTools as dt

if __name__ == "__main__":
    app = QApplication()
    win = dt.dt() 

    app.exec()