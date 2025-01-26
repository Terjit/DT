# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newWell.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_newWell(object):
    def setupUi(self, newWell):
        if not newWell.objectName():
            newWell.setObjectName(u"newWell")
        newWell.resize(442, 295)
        self.centralwidget = QWidget(newWell)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 421, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 421, 170))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.operator = QLineEdit(self.widget)
        self.operator.setObjectName(u"operator")

        self.gridLayout.addWidget(self.operator, 0, 1, 1, 7)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.wellName = QLineEdit(self.widget)
        self.wellName.setObjectName(u"wellName")

        self.gridLayout.addWidget(self.wellName, 1, 1, 1, 7)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.API = QLineEdit(self.widget)
        self.API.setObjectName(u"API")

        self.gridLayout.addWidget(self.API, 2, 1, 1, 7)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.latDeg = QLineEdit(self.widget)
        self.latDeg.setObjectName(u"latDeg")

        self.gridLayout.addWidget(self.latDeg, 3, 1, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.latMin = QLineEdit(self.widget)
        self.latMin.setObjectName(u"latMin")

        self.gridLayout.addWidget(self.latMin, 3, 3, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout.addWidget(self.label_10, 3, 4, 1, 2)

        self.latSec = QLineEdit(self.widget)
        self.latSec.setObjectName(u"latSec")

        self.gridLayout.addWidget(self.latSec, 3, 6, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout.addWidget(self.label_12, 3, 7, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.lonDeg = QLineEdit(self.widget)
        self.lonDeg.setObjectName(u"lonDeg")

        self.gridLayout.addWidget(self.lonDeg, 4, 1, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.lonSec = QLineEdit(self.widget)
        self.lonSec.setObjectName(u"lonSec")

        self.gridLayout.addWidget(self.lonSec, 4, 6, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout.addWidget(self.label_13, 4, 7, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.lonMin = QLineEdit(self.widget)
        self.lonMin.setObjectName(u"lonMin")

        self.gridLayout.addWidget(self.lonMin, 4, 3, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 4, 4, 1, 2)

        self.wellType = QComboBox(self.widget)
        self.wellType.setObjectName(u"wellType")

        self.gridLayout.addWidget(self.wellType, 5, 1, 1, 7)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 234, 421, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.openBtn = QPushButton(self.widget1)
        self.openBtn.setObjectName(u"openBtn")

        self.horizontalLayout.addWidget(self.openBtn)

        self.cancelBtn = QPushButton(self.widget1)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        newWell.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.operator, self.wellName)
        QWidget.setTabOrder(self.wellName, self.API)
        QWidget.setTabOrder(self.API, self.latDeg)
        QWidget.setTabOrder(self.latDeg, self.latMin)
        QWidget.setTabOrder(self.latMin, self.latSec)
        QWidget.setTabOrder(self.latSec, self.lonDeg)
        QWidget.setTabOrder(self.lonDeg, self.lonMin)
        QWidget.setTabOrder(self.lonMin, self.lonSec)
        QWidget.setTabOrder(self.lonSec, self.wellType)

        self.retranslateUi(newWell)

        QMetaObject.connectSlotsByName(newWell)
    # setupUi

    def retranslateUi(self, newWell):
        newWell.setWindowTitle(QCoreApplication.translate("newWell", u"Drilling Tools - Create New Well", None))
        self.label.setText(QCoreApplication.translate("newWell", u"Create New Well", None))
        self.label_2.setText(QCoreApplication.translate("newWell", u"Operator: ", None))
        self.label_3.setText(QCoreApplication.translate("newWell", u"Well Name: ", None))
        self.label_4.setText(QCoreApplication.translate("newWell", u"API #: ", None))
        self.label_5.setText(QCoreApplication.translate("newWell", u"Latitude: ", None))
        self.label_8.setText(QCoreApplication.translate("newWell", u"\u00b0", None))
        self.label_10.setText(QCoreApplication.translate("newWell", u"'", None))
        self.label_12.setText(QCoreApplication.translate("newWell", u"\"", None))
        self.label_6.setText(QCoreApplication.translate("newWell", u"Longitude: ", None))
        self.label_9.setText(QCoreApplication.translate("newWell", u"\u00b0", None))
        self.label_13.setText(QCoreApplication.translate("newWell", u"\"", None))
        self.label_7.setText(QCoreApplication.translate("newWell", u"Well Type: ", None))
        self.label_11.setText(QCoreApplication.translate("newWell", u"'", None))
        self.openBtn.setText(QCoreApplication.translate("newWell", u"Open", None))
        self.cancelBtn.setText(QCoreApplication.translate("newWell", u"Cancel", None))
    # retranslateUi

