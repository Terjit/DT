# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pva.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_pvaWindow(object):
    def setupUi(self, pvaWindow, well):
        if not pvaWindow.objectName():
            pvaWindow.setObjectName(u"pvaWindow")
        pvaWindow.resize(195, 268)
        self.centralwidget = QWidget(pvaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 171, 241))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.updatePlanBtn = QPushButton(self.widget)
        self.updatePlanBtn.setObjectName(u"updatePlanBtn")

        self.verticalLayout.addWidget(self.updatePlanBtn)

        self.updateActualBtn = QPushButton(self.widget)
        self.updateActualBtn.setObjectName(u"updateActualBtn")

        self.verticalLayout.addWidget(self.updateActualBtn)

        self.sectionBtn = QPushButton(self.widget)
        self.sectionBtn.setObjectName(u"sectionBtn")

        self.verticalLayout.addWidget(self.sectionBtn)

        self.planBtn = QPushButton(self.widget)
        self.planBtn.setObjectName(u"planBtn")

        self.verticalLayout.addWidget(self.planBtn)

        self.threedBtn = QPushButton(self.widget)
        self.threedBtn.setObjectName(u"threedBtn")

        self.verticalLayout.addWidget(self.threedBtn)

        self.formationsBox = QCheckBox(self.widget)
        self.formationsBox.setObjectName(u"formationsBox")

        self.verticalLayout.addWidget(self.formationsBox)

        pvaWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(pvaWindow, well)

        QMetaObject.connectSlotsByName(pvaWindow)
    # setupUi

    def retranslateUi(self, pvaWindow, well):
        pvaWindow.setWindowTitle(QCoreApplication.translate("pvaWindow", f"DT - PvA - {well}", None))
        self.updatePlanBtn.setText(QCoreApplication.translate("pvaWindow", u"Update Planned", None))
        self.updateActualBtn.setText(QCoreApplication.translate("pvaWindow", u"Update Actual", None))
        self.sectionBtn.setText(QCoreApplication.translate("pvaWindow", u"Section View", None))
        self.planBtn.setText(QCoreApplication.translate("pvaWindow", u"Plan View", None))
        self.threedBtn.setText(QCoreApplication.translate("pvaWindow", u"3D View", None))
        self.formationsBox.setText(QCoreApplication.translate("pvaWindow", u"Show Formations", None))
    # retranslateUi

