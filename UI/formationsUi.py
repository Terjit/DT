# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formations.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_formationWindow(object):
    def setupUi(self, formationWindow):
        if not formationWindow.objectName():
            formationWindow.setObjectName(u"formationWindow")
        formationWindow.resize(550, 658)
        font = QFont()
        font.setPointSize(8)
        formationWindow.setFont(font)
        self.centralwidget = QWidget(formationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addFormationBtn = QPushButton(self.centralwidget)
        self.addFormationBtn.setObjectName(u"addFormationBtn")
        self.addFormationBtn.setGeometry(QRect(10, 12, 221, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.addFormationBtn.setFont(font1)
        self.commitChangesBtn = QPushButton(self.centralwidget)
        self.commitChangesBtn.setObjectName(u"commitChangesBtn")
        self.commitChangesBtn.setGeometry(QRect(320, 10, 221, 41))
        self.commitChangesBtn.setFont(font1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 63, 531, 569))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.f0 = QLineEdit(self.widget)
        self.f0.setObjectName(u"f0")

        self.gridLayout.addWidget(self.f0, 1, 0, 1, 1)

        self.m0 = QLineEdit(self.widget)
        self.m0.setObjectName(u"m0")

        self.gridLayout.addWidget(self.m0, 1, 1, 1, 1)

        self.t0 = QLineEdit(self.widget)
        self.t0.setObjectName(u"t0")

        self.gridLayout.addWidget(self.t0, 1, 2, 1, 1)

        self.f1 = QLineEdit(self.widget)
        self.f1.setObjectName(u"f1")

        self.gridLayout.addWidget(self.f1, 2, 0, 1, 1)

        self.m1 = QLineEdit(self.widget)
        self.m1.setObjectName(u"m1")

        self.gridLayout.addWidget(self.m1, 2, 1, 1, 1)

        self.t1 = QLineEdit(self.widget)
        self.t1.setObjectName(u"t1")

        self.gridLayout.addWidget(self.t1, 2, 2, 1, 1)

        self.f2 = QLineEdit(self.widget)
        self.f2.setObjectName(u"f2")

        self.gridLayout.addWidget(self.f2, 3, 0, 1, 1)

        self.m2 = QLineEdit(self.widget)
        self.m2.setObjectName(u"m2")

        self.gridLayout.addWidget(self.m2, 3, 1, 1, 1)

        self.t2 = QLineEdit(self.widget)
        self.t2.setObjectName(u"t2")

        self.gridLayout.addWidget(self.t2, 3, 2, 1, 1)

        self.f3 = QLineEdit(self.widget)
        self.f3.setObjectName(u"f3")

        self.gridLayout.addWidget(self.f3, 4, 0, 1, 1)

        self.m3 = QLineEdit(self.widget)
        self.m3.setObjectName(u"m3")

        self.gridLayout.addWidget(self.m3, 4, 1, 1, 1)

        self.t3 = QLineEdit(self.widget)
        self.t3.setObjectName(u"t3")

        self.gridLayout.addWidget(self.t3, 4, 2, 1, 1)

        self.f4 = QLineEdit(self.widget)
        self.f4.setObjectName(u"f4")

        self.gridLayout.addWidget(self.f4, 5, 0, 1, 1)

        self.m4 = QLineEdit(self.widget)
        self.m4.setObjectName(u"m4")

        self.gridLayout.addWidget(self.m4, 5, 1, 1, 1)

        self.t4 = QLineEdit(self.widget)
        self.t4.setObjectName(u"t4")

        self.gridLayout.addWidget(self.t4, 5, 2, 1, 1)

        self.f5 = QLineEdit(self.widget)
        self.f5.setObjectName(u"f5")

        self.gridLayout.addWidget(self.f5, 6, 0, 1, 1)

        self.m5 = QLineEdit(self.widget)
        self.m5.setObjectName(u"m5")

        self.gridLayout.addWidget(self.m5, 6, 1, 1, 1)

        self.t5 = QLineEdit(self.widget)
        self.t5.setObjectName(u"t5")

        self.gridLayout.addWidget(self.t5, 6, 2, 1, 1)

        self.f6 = QLineEdit(self.widget)
        self.f6.setObjectName(u"f6")

        self.gridLayout.addWidget(self.f6, 7, 0, 1, 1)

        self.m6 = QLineEdit(self.widget)
        self.m6.setObjectName(u"m6")

        self.gridLayout.addWidget(self.m6, 7, 1, 1, 1)

        self.t6 = QLineEdit(self.widget)
        self.t6.setObjectName(u"t6")

        self.gridLayout.addWidget(self.t6, 7, 2, 1, 1)

        self.f7 = QLineEdit(self.widget)
        self.f7.setObjectName(u"f7")

        self.gridLayout.addWidget(self.f7, 8, 0, 1, 1)

        self.m7 = QLineEdit(self.widget)
        self.m7.setObjectName(u"m7")

        self.gridLayout.addWidget(self.m7, 8, 1, 1, 1)

        self.t7 = QLineEdit(self.widget)
        self.t7.setObjectName(u"t7")

        self.gridLayout.addWidget(self.t7, 8, 2, 1, 1)

        self.f8 = QLineEdit(self.widget)
        self.f8.setObjectName(u"f8")

        self.gridLayout.addWidget(self.f8, 9, 0, 1, 1)

        self.m8 = QLineEdit(self.widget)
        self.m8.setObjectName(u"m8")

        self.gridLayout.addWidget(self.m8, 9, 1, 1, 1)

        self.t8 = QLineEdit(self.widget)
        self.t8.setObjectName(u"t8")

        self.gridLayout.addWidget(self.t8, 9, 2, 1, 1)

        self.f9 = QLineEdit(self.widget)
        self.f9.setObjectName(u"f9")

        self.gridLayout.addWidget(self.f9, 10, 0, 1, 1)

        self.m9 = QLineEdit(self.widget)
        self.m9.setObjectName(u"m9")

        self.gridLayout.addWidget(self.m9, 10, 1, 1, 1)

        self.t9 = QLineEdit(self.widget)
        self.t9.setObjectName(u"t9")

        self.gridLayout.addWidget(self.t9, 10, 2, 1, 1)

        self.f10 = QLineEdit(self.widget)
        self.f10.setObjectName(u"f10")

        self.gridLayout.addWidget(self.f10, 11, 0, 1, 1)

        self.m10 = QLineEdit(self.widget)
        self.m10.setObjectName(u"m10")

        self.gridLayout.addWidget(self.m10, 11, 1, 1, 1)

        self.t10 = QLineEdit(self.widget)
        self.t10.setObjectName(u"t10")

        self.gridLayout.addWidget(self.t10, 11, 2, 1, 1)

        self.f11 = QLineEdit(self.widget)
        self.f11.setObjectName(u"f11")

        self.gridLayout.addWidget(self.f11, 12, 0, 1, 1)

        self.m11 = QLineEdit(self.widget)
        self.m11.setObjectName(u"m11")

        self.gridLayout.addWidget(self.m11, 12, 1, 1, 1)

        self.t11 = QLineEdit(self.widget)
        self.t11.setObjectName(u"t11")

        self.gridLayout.addWidget(self.t11, 12, 2, 1, 1)

        self.f12 = QLineEdit(self.widget)
        self.f12.setObjectName(u"f12")

        self.gridLayout.addWidget(self.f12, 13, 0, 1, 1)

        self.m12 = QLineEdit(self.widget)
        self.m12.setObjectName(u"m12")

        self.gridLayout.addWidget(self.m12, 13, 1, 1, 1)

        self.t12 = QLineEdit(self.widget)
        self.t12.setObjectName(u"t12")

        self.gridLayout.addWidget(self.t12, 13, 2, 1, 1)

        self.f13 = QLineEdit(self.widget)
        self.f13.setObjectName(u"f13")

        self.gridLayout.addWidget(self.f13, 14, 0, 1, 1)

        self.m13 = QLineEdit(self.widget)
        self.m13.setObjectName(u"m13")

        self.gridLayout.addWidget(self.m13, 14, 1, 1, 1)

        self.t13 = QLineEdit(self.widget)
        self.t13.setObjectName(u"t13")

        self.gridLayout.addWidget(self.t13, 14, 2, 1, 1)

        self.f14 = QLineEdit(self.widget)
        self.f14.setObjectName(u"f14")

        self.gridLayout.addWidget(self.f14, 15, 0, 1, 1)

        self.m14 = QLineEdit(self.widget)
        self.m14.setObjectName(u"m14")

        self.gridLayout.addWidget(self.m14, 15, 1, 1, 1)

        self.t14 = QLineEdit(self.widget)
        self.t14.setObjectName(u"t14")

        self.gridLayout.addWidget(self.t14, 15, 2, 1, 1)

        self.f15 = QLineEdit(self.widget)
        self.f15.setObjectName(u"f15")

        self.gridLayout.addWidget(self.f15, 16, 0, 1, 1)

        self.m15 = QLineEdit(self.widget)
        self.m15.setObjectName(u"m15")

        self.gridLayout.addWidget(self.m15, 16, 1, 1, 1)

        self.t15 = QLineEdit(self.widget)
        self.t15.setObjectName(u"t15")

        self.gridLayout.addWidget(self.t15, 16, 2, 1, 1)

        self.f16 = QLineEdit(self.widget)
        self.f16.setObjectName(u"f16")

        self.gridLayout.addWidget(self.f16, 17, 0, 1, 1)

        self.m16 = QLineEdit(self.widget)
        self.m16.setObjectName(u"m16")

        self.gridLayout.addWidget(self.m16, 17, 1, 1, 1)

        self.t16 = QLineEdit(self.widget)
        self.t16.setObjectName(u"t16")

        self.gridLayout.addWidget(self.t16, 17, 2, 1, 1)

        self.f17 = QLineEdit(self.widget)
        self.f17.setObjectName(u"f17")

        self.gridLayout.addWidget(self.f17, 18, 0, 1, 1)

        self.m17 = QLineEdit(self.widget)
        self.m17.setObjectName(u"m17")

        self.gridLayout.addWidget(self.m17, 18, 1, 1, 1)

        self.t17 = QLineEdit(self.widget)
        self.t17.setObjectName(u"t17")

        self.gridLayout.addWidget(self.t17, 18, 2, 1, 1)

        self.f18 = QLineEdit(self.widget)
        self.f18.setObjectName(u"f18")

        self.gridLayout.addWidget(self.f18, 19, 0, 1, 1)

        self.m18 = QLineEdit(self.widget)
        self.m18.setObjectName(u"m18")

        self.gridLayout.addWidget(self.m18, 19, 1, 1, 1)

        self.t18 = QLineEdit(self.widget)
        self.t18.setObjectName(u"t18")

        self.gridLayout.addWidget(self.t18, 19, 2, 1, 1)

        self.f19 = QLineEdit(self.widget)
        self.f19.setObjectName(u"f19")

        self.gridLayout.addWidget(self.f19, 20, 0, 1, 1)

        self.m19 = QLineEdit(self.widget)
        self.m19.setObjectName(u"m19")

        self.gridLayout.addWidget(self.m19, 20, 1, 1, 1)

        self.t19 = QLineEdit(self.widget)
        self.t19.setObjectName(u"t19")

        self.gridLayout.addWidget(self.t19, 20, 2, 1, 1)

        self.f20 = QLineEdit(self.widget)
        self.f20.setObjectName(u"f20")

        self.gridLayout.addWidget(self.f20, 21, 0, 1, 1)

        self.m20 = QLineEdit(self.widget)
        self.m20.setObjectName(u"m20")

        self.gridLayout.addWidget(self.m20, 21, 1, 1, 1)

        self.t20 = QLineEdit(self.widget)
        self.t20.setObjectName(u"t20")

        self.gridLayout.addWidget(self.t20, 21, 2, 1, 1)

        formationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(formationWindow)

        QMetaObject.connectSlotsByName(formationWindow)
    # setupUi

    def retranslateUi(self, formationWindow):
        formationWindow.setWindowTitle(QCoreApplication.translate("formationWindow", u"newWindow", None))
        self.addFormationBtn.setText(QCoreApplication.translate("formationWindow", u"Add Formation", None))
        self.commitChangesBtn.setText(QCoreApplication.translate("formationWindow", u"Commit Changes", None))
        self.label.setText(QCoreApplication.translate("formationWindow", u"Formation Name", None))
        self.label_2.setText(QCoreApplication.translate("formationWindow", u"Measured Depth", None))
        self.label_3.setText(QCoreApplication.translate("formationWindow", u"True Vertical Depth", None))
    # retranslateUi

