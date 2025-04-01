# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateDir.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_updateDirWin(object):
    def setupUi(self, updateDirWin, well):
        if not updateDirWin.objectName():
            updateDirWin.setObjectName(u"updateDirWin")
        updateDirWin.resize(195, 152)
        self.centralwidget = QWidget(updateDirWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 171, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.updatePlanBtn = QPushButton(self.layoutWidget)
        self.updatePlanBtn.setObjectName(u"updatePlanBtn")

        self.verticalLayout.addWidget(self.updatePlanBtn)

        self.updateActualBtn = QPushButton(self.layoutWidget)
        self.updateActualBtn.setObjectName(u"updateActualBtn")

        self.verticalLayout.addWidget(self.updateActualBtn)

        self.lateralBtn = QPushButton(self.layoutWidget)
        self.lateralBtn.setObjectName(u"lateralBtn")

        self.verticalLayout.addWidget(self.lateralBtn)

        updateDirWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(updateDirWin, well)

        QMetaObject.connectSlotsByName(updateDirWin)
    # setupUi

    def retranslateUi(self, updateDirWin, well):
        updateDirWin.setWindowTitle(QCoreApplication.translate("updateDirWin", f"DT - UD - {well}", None))
        self.updatePlanBtn.setText(QCoreApplication.translate("updateDirWin", u"Add/Update Planned", None))
        self.updateActualBtn.setText(QCoreApplication.translate("updateDirWin", u"Add/Update Actual", None))
        self.lateralBtn.setText(QCoreApplication.translate("updateDirWin", u"Add/Update Lateral", None))
    # retranslateUi

