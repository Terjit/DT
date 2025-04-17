# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addCasing.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_addCasing(object):
    def setupUi(self, addCasing, well):
        if not addCasing.objectName():
            addCasing.setObjectName(u"addCasing")
        addCasing.resize(696, 113)
        self.centralwidget = QWidget(addCasing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(520, 70, 158, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.submitBtn = QPushButton(self.layoutWidget)
        self.submitBtn.setObjectName(u"submitBtn")

        self.horizontalLayout.addWidget(self.submitBtn)

        self.cancelBtn = QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 671, 48))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)

        self.holeDia = QLineEdit(self.layoutWidget1)
        self.holeDia.setObjectName(u"holeDia")

        self.gridLayout.addWidget(self.holeDia, 1, 0, 1, 1)

        self.OdBox = QComboBox(self.layoutWidget1)
        self.OdBox.setObjectName(u"OdBox")

        self.gridLayout.addWidget(self.OdBox, 1, 1, 1, 1)

        self.weightBox = QComboBox(self.layoutWidget1)
        self.weightBox.setObjectName(u"weightBox")

        self.gridLayout.addWidget(self.weightBox, 1, 2, 1, 1)

        self.gradeBox = QComboBox(self.layoutWidget1)
        self.gradeBox.setObjectName(u"gradeBox")

        self.gridLayout.addWidget(self.gradeBox, 1, 3, 1, 1)

        self.casingTop = QLineEdit(self.layoutWidget1)
        self.casingTop.setObjectName(u"casingTop")

        self.gridLayout.addWidget(self.casingTop, 1, 4, 1, 1)

        self.casingBottom = QLineEdit(self.layoutWidget1)
        self.casingBottom.setObjectName(u"casingBottom")

        self.gridLayout.addWidget(self.casingBottom, 1, 5, 1, 1)

        addCasing.setCentralWidget(self.centralwidget)

        self.retranslateUi(addCasing, well)

        QMetaObject.connectSlotsByName(addCasing)
    # setupUi

    def retranslateUi(self, addCasing, well):
        addCasing.setWindowTitle(QCoreApplication.translate("addCasing", f"Drilling Tools - Add Casing - {well}", None))
        self.submitBtn.setText(QCoreApplication.translate("addCasing", u"Submit", None))
        self.cancelBtn.setText(QCoreApplication.translate("addCasing", u"Cancel", None))
        self.label_6.setText(QCoreApplication.translate("addCasing", u"Hole Diameter", None))
        self.label.setText(QCoreApplication.translate("addCasing", u"Casing OD", None))
        self.label_2.setText(QCoreApplication.translate("addCasing", u"Casing Weight", None))
        self.label_3.setText(QCoreApplication.translate("addCasing", u"Casing Grade", None))
        self.label_4.setText(QCoreApplication.translate("addCasing", u"Casing Top", None))
        self.label_5.setText(QCoreApplication.translate("addCasing", u"Casing Bottom", None))
    # retranslateUi

