# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'outputDirReport.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, well):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(195, 259)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 191, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 61, 171, 191))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.widget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.generateBtn = QPushButton(self.widget)
        self.generateBtn.setObjectName(u"generateBtn")

        self.verticalLayout.addWidget(self.generateBtn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, well)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow, well):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", f"DT - OD - {well}", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Items It Output", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Cover Page", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Plan - Section View", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Plan - TVD vs. MD View", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Plan - Plan View", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Plan - Directional Data", None))
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

