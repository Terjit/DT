# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    def setupUi(self, chartWindow):
        if not chartWindow.objectName():
            chartWindow.setObjectName(u"chartWindow")
        chartWindow.resize(195, 184)
        self.centralwidget = QWidget(chartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 15, 172, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sectionBtn = QPushButton(self.widget)
        self.sectionBtn.setObjectName(u"sectionBtn")
        font = QFont()
        font.setPointSize(8)
        self.sectionBtn.setFont(font)

        self.verticalLayout.addWidget(self.sectionBtn)

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

        self.retranslateUi(chartWindow)

        QMetaObject.connectSlotsByName(chartWindow)
    # setupUi

    def retranslateUi(self, chartWindow):
        chartWindow.setWindowTitle(QCoreApplication.translate("chartWindow", u"DT - WPE - Chart View - {well}", None))
        self.sectionBtn.setText(QCoreApplication.translate("chartWindow", u"Section View", None))
        self.planBtn.setText(QCoreApplication.translate("chartWindow", u"Plan View", None))
        self.threedBtn.setText(QCoreApplication.translate("chartWindow", u"3D View", None))
        self.formationsBox.setText(QCoreApplication.translate("chartWindow", u"Show Formations", None))
    # retranslateUi

