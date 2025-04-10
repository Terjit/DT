# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addLateralName.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_updateLatNameWin(object):
    def setupUi(self, updateLatNameWin, well):
        if not updateLatNameWin.objectName():
            updateLatNameWin.setObjectName(u"updateLatNameWin")
        updateLatNameWin.resize(225, 173)
        font = QFont()
        font.setPointSize(5)
        updateLatNameWin.setFont(font)
        self.centralwidget = QWidget(updateLatNameWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, -10, 301, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 81, 31))
        self.label_2.setFont(font1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 40, 113, 31))
        self.lineEdit.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 120, 201, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addLateralBtn = QPushButton(self.layoutWidget)
        self.addLateralBtn.setObjectName(u"addLateralBtn")
        font2 = QFont()
        font2.setPointSize(9)
        self.addLateralBtn.setFont(font2)

        self.horizontalLayout.addWidget(self.addLateralBtn)

        self.cancelBtn = QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setFont(font2)

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 91, 211, 21))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plannedBox = QCheckBox(self.widget)
        self.plannedBox.setObjectName(u"plannedBox")
        self.plannedBox.setFont(font2)

        self.horizontalLayout_2.addWidget(self.plannedBox)

        self.actualBox = QCheckBox(self.widget)
        self.actualBox.setObjectName(u"actualBox")
        self.actualBox.setFont(font2)

        self.horizontalLayout_2.addWidget(self.actualBox)

        updateLatNameWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(updateLatNameWin, well)

        QMetaObject.connectSlotsByName(updateLatNameWin)
    # setupUi

    def retranslateUi(self, updateLatNameWin, well):
        updateLatNameWin.setWindowTitle(QCoreApplication.translate("updateLatNameWin", f"DT - LN - {well}", None))
        self.label.setText(QCoreApplication.translate("updateLatNameWin", u"Add Lateral Name", None))
        self.label_2.setText(QCoreApplication.translate("updateLatNameWin", f"{well}", None))
        self.lineEdit.setText("")
        self.addLateralBtn.setText(QCoreApplication.translate("updateLatNameWin", u"Add/Update Lateral", None))
        self.cancelBtn.setText(QCoreApplication.translate("updateLatNameWin", u"Cancel", None))
        self.plannedBox.setText(QCoreApplication.translate("updateLatNameWin", u"Planned", None))
        self.actualBox.setText(QCoreApplication.translate("updateLatNameWin", u"Actual", None))
    # retranslateUi

