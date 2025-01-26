# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DT.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_newWell(object):
    def setupUi(self, newWell):
        if not newWell.objectName():
            newWell.setObjectName(u"newWell")
        newWell.resize(442, 159)
        self.centralwidget = QWidget(newWell)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 421, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 90, 401, 51))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.createWell = QPushButton(self.widget)
        self.createWell.setObjectName(u"createWell")

        self.horizontalLayout.addWidget(self.createWell)

        self.openWell = QPushButton(self.widget)
        self.openWell.setObjectName(u"openWell")

        self.horizontalLayout.addWidget(self.openWell)

        newWell.setCentralWidget(self.centralwidget)

        self.retranslateUi(newWell)

        QMetaObject.connectSlotsByName(newWell)
    # setupUi

    def retranslateUi(self, newWell):
        newWell.setWindowTitle(QCoreApplication.translate("newWell", u"Drilling Tools - Select Well", None))
        self.label.setText(QCoreApplication.translate("newWell", u"Create new well or open exisiting well", None))
        self.createWell.setText(QCoreApplication.translate("newWell", u"Create New Well", None))
        self.openWell.setText(QCoreApplication.translate("newWell", u"Open Existing Well", None))
    # retranslateUi

