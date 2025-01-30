# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWell.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_addWell(object):
    def setupUi(self, addWell):
        if not addWell.objectName():
            addWell.setObjectName(u"addWell")
        addWell.resize(267, 152)
        self.centralwidget = QWidget(addWell)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 12, 229, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.addWellBtn = QPushButton(self.widget)
        self.addWellBtn.setObjectName(u"addWellBtn")

        self.verticalLayout.addWidget(self.addWellBtn)

        self.cancelBtn = QPushButton(self.widget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.verticalLayout.addWidget(self.cancelBtn)

        addWell.setCentralWidget(self.centralwidget)

        self.retranslateUi(addWell)

        QMetaObject.connectSlotsByName(addWell)
    # setupUi

    def retranslateUi(self, addWell):
        addWell.setWindowTitle(QCoreApplication.translate("addWell", u"DT - WE - PV - Add Well", None))
        self.label.setText(QCoreApplication.translate("addWell", u"Select well to add to pad view", None))
        self.addWellBtn.setText(QCoreApplication.translate("addWell", u"Add Well", None))
        self.cancelBtn.setText(QCoreApplication.translate("addWell", u"Cancel ", None))
    # retranslateUi

