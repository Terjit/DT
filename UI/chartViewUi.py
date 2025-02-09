# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_chartWindow(object):
    def setupUi(self, chartWindow, well):
        if not chartWindow.objectName():
            chartWindow.setObjectName(u"chartWindow")
        chartWindow.resize(195, 239)
        self.centralwidget = QWidget(chartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 13, 171, 211))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sectionBtn = QPushButton(self.widget)
        self.sectionBtn.setObjectName(u"sectionBtn")
        font = QFont()
        font.setPointSize(8)
        self.sectionBtn.setFont(font)

        self.verticalLayout.addWidget(self.sectionBtn)

        self.tvdBtn = QPushButton(self.widget)
        self.tvdBtn.setObjectName(u"tvdBtn")

        self.verticalLayout.addWidget(self.tvdBtn)

        self.planBtn = QPushButton(self.widget)
        self.planBtn.setObjectName(u"planBtn")

        self.verticalLayout.addWidget(self.planBtn)

        self.threedBtn = QPushButton(self.widget)
        self.threedBtn.setObjectName(u"threedBtn")

        self.verticalLayout.addWidget(self.threedBtn)

        self.formationsBox = QCheckBox(self.widget)
        self.formationsBox.setObjectName(u"formationsBox")
        font1 = QFont()
        font1.setPointSize(12)
        self.formationsBox.setFont(font1)

        self.verticalLayout.addWidget(self.formationsBox)

        chartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(chartWindow, well)

        QMetaObject.connectSlotsByName(chartWindow)
    # setupUi

    def retranslateUi(self, chartWindow, well):
        chartWindow.setWindowTitle(QCoreApplication.translate("chartWindow", f"DT - WPE - Chart View - {well}", None))
        self.sectionBtn.setText(QCoreApplication.translate("chartWindow", u"Section View", None))
        self.tvdBtn.setText(QCoreApplication.translate("chartWindow", u"TVD vs. MD", None))
        self.planBtn.setText(QCoreApplication.translate("chartWindow", u"Plan View", None))
        self.threedBtn.setText(QCoreApplication.translate("chartWindow", u"3D View", None))
        self.formationsBox.setText(QCoreApplication.translate("chartWindow", u"Show Formations", None))
    # retranslateUi

