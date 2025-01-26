# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'existingWell.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_openExistingWindow(object):
    def setupUi(self, openExistingWindow):
        if not openExistingWindow.objectName():
            openExistingWindow.setObjectName(u"openExistingWindow")
        openExistingWindow.resize(442, 196)
        self.centralwidget = QWidget(openExistingWindow)
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
        self.widget.setGeometry(QRect(20, 80, 401, 61))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.operatorBox = QComboBox(self.widget)
        self.operatorBox.setObjectName(u"operatorBox")

        self.gridLayout.addWidget(self.operatorBox, 1, 0, 1, 1)

        self.wellBox = QComboBox(self.widget)
        self.wellBox.setObjectName(u"wellBox")

        self.gridLayout.addWidget(self.wellBox, 1, 1, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 144, 401, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.openBtn = QPushButton(self.widget1)
        self.openBtn.setObjectName(u"openBtn")

        self.horizontalLayout.addWidget(self.openBtn)

        self.cancelBtn = QPushButton(self.widget1)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        openExistingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(openExistingWindow)

        QMetaObject.connectSlotsByName(openExistingWindow)
    # setupUi

    def retranslateUi(self, openExistingWindow):
        openExistingWindow.setWindowTitle(QCoreApplication.translate("openExistingWindow", u"Drilling Tools - Open Existing Well", None))
        self.label.setText(QCoreApplication.translate("openExistingWindow", u"Open Existing Well", None))
        self.label_2.setText(QCoreApplication.translate("openExistingWindow", u"Operator", None))
        self.label_3.setText(QCoreApplication.translate("openExistingWindow", u"Well", None))
        self.openBtn.setText(QCoreApplication.translate("openExistingWindow", u"Open", None))
        self.cancelBtn.setText(QCoreApplication.translate("openExistingWindow", u"Cancel", None))
    # retranslateUi

