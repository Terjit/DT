# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_selectionWindow(object):
    def setupUi(self, selectionWindow):
        if not selectionWindow.objectName():
            selectionWindow.setObjectName(u"selectionWindow")
        selectionWindow.resize(195, 589)
        self.centralwidget = QWidget(selectionWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wellName = QLabel(self.centralwidget)
        self.wellName.setObjectName(u"wellName")
        self.wellName.setGeometry(QRect(10, 10, 171, 21))
        font = QFont()
        font.setPointSize(16)
        self.wellName.setFont(font)
        self.wellName.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 171, 541))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formationBtn = QPushButton(self.widget)
        self.formationBtn.setObjectName(u"formationBtn")

        self.verticalLayout.addWidget(self.formationBtn)

        self.wellPathBtn = QPushButton(self.widget)
        self.wellPathBtn.setObjectName(u"wellPathBtn")

        self.verticalLayout.addWidget(self.wellPathBtn)

        self.wellBuilderBtn = QPushButton(self.widget)
        self.wellBuilderBtn.setObjectName(u"wellBuilderBtn")

        self.verticalLayout.addWidget(self.wellBuilderBtn)

        self.cementingBtn = QPushButton(self.widget)
        self.cementingBtn.setObjectName(u"cementingBtn")

        self.verticalLayout.addWidget(self.cementingBtn)

        self.bhaBtn = QPushButton(self.widget)
        self.bhaBtn.setObjectName(u"bhaBtn")

        self.verticalLayout.addWidget(self.bhaBtn)

        self.rigBtn = QPushButton(self.widget)
        self.rigBtn.setObjectName(u"rigBtn")

        self.verticalLayout.addWidget(self.rigBtn)

        self.fluidsBtn = QPushButton(self.widget)
        self.fluidsBtn.setObjectName(u"fluidsBtn")

        self.verticalLayout.addWidget(self.fluidsBtn)

        self.hydraulicsBtn = QPushButton(self.widget)
        self.hydraulicsBtn.setObjectName(u"hydraulicsBtn")

        self.verticalLayout.addWidget(self.hydraulicsBtn)

        self.tdBtn = QPushButton(self.widget)
        self.tdBtn.setObjectName(u"tdBtn")

        self.verticalLayout.addWidget(self.tdBtn)

        self.casingPicksBtn = QPushButton(self.widget)
        self.casingPicksBtn.setObjectName(u"casingPicksBtn")

        self.verticalLayout.addWidget(self.casingPicksBtn)

        self.circBtn = QPushButton(self.widget)
        self.circBtn.setObjectName(u"circBtn")

        self.verticalLayout.addWidget(self.circBtn)

        self.editWellBtn = QPushButton(self.widget)
        self.editWellBtn.setObjectName(u"editWellBtn")

        self.verticalLayout.addWidget(self.editWellBtn)

        self.changeWellBtn = QPushButton(self.widget)
        self.changeWellBtn.setObjectName(u"changeWellBtn")

        self.verticalLayout.addWidget(self.changeWellBtn)

        selectionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectionWindow)

        QMetaObject.connectSlotsByName(selectionWindow)
    # setupUi

    def retranslateUi(self, selectionWindow):
        selectionWindow.setWindowTitle(QCoreApplication.translate("selectionWindow", u"DT - Select App", None))
        self.wellName.setText(QCoreApplication.translate("selectionWindow", u"Well Name", None))
        self.formationBtn.setText(QCoreApplication.translate("selectionWindow", u"Formation Editor", None))
        self.wellPathBtn.setText(QCoreApplication.translate("selectionWindow", u"Well Path Editor", None))
        self.wellBuilderBtn.setText(QCoreApplication.translate("selectionWindow", u"Well Builder", None))
        self.cementingBtn.setText(QCoreApplication.translate("selectionWindow", u"Cementing", None))
        self.bhaBtn.setText(QCoreApplication.translate("selectionWindow", u"BHA Editor", None))
        self.rigBtn.setText(QCoreApplication.translate("selectionWindow", u"Rig Information Editor", None))
        self.fluidsBtn.setText(QCoreApplication.translate("selectionWindow", u"Fluids Editor", None))
        self.hydraulicsBtn.setText(QCoreApplication.translate("selectionWindow", u"Hydraulics", None))
        self.tdBtn.setText(QCoreApplication.translate("selectionWindow", u"Torque + Drag", None))
        self.casingPicksBtn.setText(QCoreApplication.translate("selectionWindow", u"Casing Picks", None))
        self.circBtn.setText(QCoreApplication.translate("selectionWindow", u"Circulation Times", None))
        self.editWellBtn.setText(QCoreApplication.translate("selectionWindow", u"Edit Well", None))
        self.changeWellBtn.setText(QCoreApplication.translate("selectionWindow", u"Change Well", None))
    # retranslateUi

