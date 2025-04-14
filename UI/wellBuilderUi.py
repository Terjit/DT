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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_wellBuilder(object):
    def setupUi(self, wellBuilder, well):
        if not wellBuilder.objectName():
            wellBuilder.setObjectName(u"wellBuilder")
        wellBuilder.resize(195, 334)
        self.centralwidget = QWidget(wellBuilder)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wellName = QLabel(self.centralwidget)
        self.wellName.setObjectName(u"wellName")
        self.wellName.setGeometry(QRect(10, 10, 171, 21))
        font = QFont()
        font.setPointSize(16)
        self.wellName.setFont(font)
        self.wellName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 171, 291))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.surfaceBtn = QPushButton(self.widget)
        self.surfaceBtn.setObjectName(u"surfaceBtn")

        self.verticalLayout.addWidget(self.surfaceBtn)

        self.intBtn = QPushButton(self.widget)
        self.intBtn.setObjectName(u"intBtn")

        self.verticalLayout.addWidget(self.intBtn)

        self.prodBtn = QPushButton(self.widget)
        self.prodBtn.setObjectName(u"prodBtn")

        self.verticalLayout.addWidget(self.prodBtn)

        self.lineBtn = QPushButton(self.widget)
        self.lineBtn.setObjectName(u"lineBtn")

        self.verticalLayout.addWidget(self.lineBtn)

        self.tubeBtn = QPushButton(self.widget)
        self.tubeBtn.setObjectName(u"tubeBtn")

        self.verticalLayout.addWidget(self.tubeBtn)

        self.tapeBtn = QPushButton(self.widget)
        self.tapeBtn.setObjectName(u"tapeBtn")

        self.verticalLayout.addWidget(self.tapeBtn)

        wellBuilder.setCentralWidget(self.centralwidget)

        self.retranslateUi(wellBuilder, well)

        QMetaObject.connectSlotsByName(wellBuilder)
    # setupUi

    def retranslateUi(self, wellBuilder, well):
        wellBuilder.setWindowTitle(QCoreApplication.translate("wellBuilder", f"DT - WB - {well}", None))
        self.wellName.setText(QCoreApplication.translate("wellBuilder", f"{well}", None))
        self.surfaceBtn.setText(QCoreApplication.translate("wellBuilder", u"Surface Casing", None))
        self.intBtn.setText(QCoreApplication.translate("wellBuilder", u"Intermediate Casing", None))
        self.prodBtn.setText(QCoreApplication.translate("wellBuilder", u"Production Casing", None))
        self.lineBtn.setText(QCoreApplication.translate("wellBuilder", u"Liner", None))
        self.tubeBtn.setText(QCoreApplication.translate("wellBuilder", u"Tubing", None))
        self.tapeBtn.setText(QCoreApplication.translate("wellBuilder", u"Tapered String", None))
    # retranslateUi

