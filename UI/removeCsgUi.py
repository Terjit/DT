# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removeCsg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_removeCsg(object):
    def setupUi(self, removeCsg, well):
        if not removeCsg.objectName():
            removeCsg.setObjectName(u"removeCsg")
        removeCsg.resize(204, 279)
        self.centralwidget = QWidget(removeCsg)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 171, 211))
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

        self.checkBox_6 = QCheckBox(self.widget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 230, 171, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.removeBtn = QPushButton(self.widget1)
        self.removeBtn.setObjectName(u"removeBtn")

        self.horizontalLayout.addWidget(self.removeBtn)

        self.cancelBtn = QPushButton(self.widget1)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        removeCsg.setCentralWidget(self.centralwidget)

        self.retranslateUi(removeCsg, well)

        QMetaObject.connectSlotsByName(removeCsg)
    # setupUi

    def retranslateUi(self, removeCsg, well):
        removeCsg.setWindowTitle(QCoreApplication.translate("removeCsg", f"DT - WB - Remove Casing - {well}", None))
        self.checkBox.setText(QCoreApplication.translate("removeCsg", u"Conductor", None))
        self.checkBox_2.setText(QCoreApplication.translate("removeCsg", u"Surface", None))
        self.checkBox_3.setText(QCoreApplication.translate("removeCsg", u"Intermediate", None))
        self.checkBox_4.setText(QCoreApplication.translate("removeCsg", u"Liner", None))
        self.checkBox_5.setText(QCoreApplication.translate("removeCsg", u"Production", None))
        self.checkBox_6.setText(QCoreApplication.translate("removeCsg", u"Tubing", None))
        self.removeBtn.setText(QCoreApplication.translate("removeCsg", u"Remove", None))
        self.cancelBtn.setText(QCoreApplication.translate("removeCsg", u"Cancel", None))
    # retranslateUi

