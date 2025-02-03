# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'padView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_padView(object):
    def setupUi(self, padView, pad):
        if not padView.objectName():
            padView.setObjectName(u"padView")
        padView.resize(195, 425)
        self.centralwidget = QWidget(padView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 80, 173, 61))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 171, 59))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 18, 171, 52))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addWellBtn = QPushButton(self.widget)
        self.addWellBtn.setObjectName(u"addWellBtn")

        self.verticalLayout.addWidget(self.addWellBtn)

        self.annotationsBox = QCheckBox(self.widget)
        self.annotationsBox.setObjectName(u"annotationsBox")

        self.verticalLayout.addWidget(self.annotationsBox)

        padView.setCentralWidget(self.centralwidget)

        self.retranslateUi(padView, pad)

        QMetaObject.connectSlotsByName(padView)
    # setupUi

    def retranslateUi(self, padView, pad):
        padView.setWindowTitle(QCoreApplication.translate("padView", f"DT - Pad View - {pad}", None))
        self.label_3.setText(QCoreApplication.translate("padView", u"Highlight", None))
        self.label.setText(QCoreApplication.translate("padView", u"Show", None))
        self.label_2.setText(QCoreApplication.translate("padView", u"Well", None))
        self.addWellBtn.setText(QCoreApplication.translate("padView", u"Add Well", None))
        self.annotationsBox.setText(QCoreApplication.translate("padView", u"Show Well Annotations", None))
    # retranslateUi

