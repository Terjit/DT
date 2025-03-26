# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateCsv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_updateCsvWindow(object):
    def setupUi(self, importCsvWindow, well):
        if not importCsvWindow.objectName():
            importCsvWindow.setObjectName(u"importCsvWindow")
        importCsvWindow.resize(537, 151)
        self.centralwidget = QWidget(importCsvWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -1, 521, 61))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.importBtn = QPushButton(self.centralwidget)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(10, 80, 81, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 60, 191, 81))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 30, 191, 31))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.cancelBtn = QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(120, 80, 81, 31))
        importCsvWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(importCsvWindow, well)

        QMetaObject.connectSlotsByName(importCsvWindow)
    # setupUi

    def retranslateUi(self, importCsvWindow, well):
        importCsvWindow.setWindowTitle(QCoreApplication.translate("importCsvWindow", f"Drilling Tools - Import CSV - {well}", None))
        self.label.setText(QCoreApplication.translate("importCsvWindow", f"<html><head/><body><p>Update deviation information {well}. </p><p>Please import a .CSV</p></body></html>", None))
        self.importBtn.setText(QCoreApplication.translate("importCsvWindow", u"Import .csv", None))
        self.label_2.setText(QCoreApplication.translate("importCsvWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("importCsvWindow", u".csv must be in the below format", None))
        self.cancelBtn.setText(QCoreApplication.translate("importCsvWindow", u"Cancel", None))
    # retranslateUi

