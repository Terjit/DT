# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wellBuilder.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

class Ui_wellBuilder(object):
    def setupUi(self, wellBuilder, well='None'):
        if not wellBuilder.objectName():
            wellBuilder.setObjectName(u"wellBuilder")
        wellBuilder.resize(195, 600)
        self.centralwidget = QWidget(wellBuilder)
        self.centralwidget.setObjectName(u"centralwidget")
        wellBuilder.setCentralWidget(self.centralwidget)

        self.retranslateUi(wellBuilder, well)

        QMetaObject.connectSlotsByName(wellBuilder)
    # setupUi

    def retranslateUi(self, wellBuilder, well):
        wellBuilder.setWindowTitle(QCoreApplication.translate("wellBuilder", f"DT - WB - {well}", None))
    # retranslateUi

