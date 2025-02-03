# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wellPath.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_wellPathWindow(object):
    def setupUi(self, wellPathWindow, well):
        if not wellPathWindow.objectName():
            wellPathWindow.setObjectName(u"wellPathWindow")
        wellPathWindow.resize(195, 269)
        self.centralwidget = QWidget(wellPathWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 9, 171, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.chartBtn = QPushButton(self.layoutWidget)
        self.chartBtn.setObjectName(u"chartBtn")

        self.verticalLayout.addWidget(self.chartBtn)

        self.padBtn = QPushButton(self.layoutWidget)
        self.padBtn.setObjectName(u"padBtn")

        self.verticalLayout.addWidget(self.padBtn)

        self.planVactualBtn = QPushButton(self.layoutWidget)
        self.planVactualBtn.setObjectName(u"planVactualBtn")

        self.verticalLayout.addWidget(self.planVactualBtn)

        self.pdfBtn = QPushButton(self.layoutWidget)
        self.pdfBtn.setObjectName(u"pdfBtn")

        self.verticalLayout.addWidget(self.pdfBtn)

        self.updateBtn = QPushButton(self.layoutWidget)
        self.updateBtn.setObjectName(u"updateBtn")

        self.verticalLayout.addWidget(self.updateBtn)

        self.exportBtn = QPushButton(self.layoutWidget)
        self.exportBtn.setObjectName(u"exportBtn")

        self.verticalLayout.addWidget(self.exportBtn)

        wellPathWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(wellPathWindow, well)

        QMetaObject.connectSlotsByName(wellPathWindow)
    # setupUi

    def retranslateUi(self, wellPathWindow, well):
        wellPathWindow.setWindowTitle(QCoreApplication.translate(u"wellPathWindow", f"DT - Well Path Editor - {well}", None))
        self.chartBtn.setText(QCoreApplication.translate("wellPathWindow", u"Chart View", None))
        self.padBtn.setText(QCoreApplication.translate("wellPathWindow", u"Pad View", None))
        self.planVactualBtn.setText(QCoreApplication.translate("wellPathWindow", u"Plan vs. Actual", None))
        self.pdfBtn.setText(QCoreApplication.translate("wellPathWindow", u"Generate PDF Report", None))
        self.updateBtn.setText(QCoreApplication.translate("wellPathWindow", u"Update Dirrectional Data", None))
        self.exportBtn.setText(QCoreApplication.translate("wellPathWindow", u"Export .csv", None))
    # retranslateUi

