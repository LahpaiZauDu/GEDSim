# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectsubject.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget, QWizardPage)

class Ui_SelectSubject(object):
    def setupUi(self, SelectSubject):
        if not SelectSubject.objectName():
            SelectSubject.setObjectName(u"SelectSubject")
        SelectSubject.resize(657, 476)
        SelectSubject.setMinimumSize(QSize(657, 476))
        SelectSubject.setMaximumSize(QSize(657, 476))
        SelectSubject.setBaseSize(QSize(0, 0))
        self.MathPushButton = QPushButton(SelectSubject)
        self.MathPushButton.setObjectName(u"MathPushButton")
        self.MathPushButton.setGeometry(QRect(93, 190, 90, 74))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MathPushButton.sizePolicy().hasHeightForWidth())
        self.MathPushButton.setSizePolicy(sizePolicy)
        self.MathPushButton.setSizeIncrement(QSize(0, 0))
        self.MathPushButton.setAutoDefault(False)
        self.MathPushButton.setFlat(False)
        self.EngPushButton = QPushButton(SelectSubject)
        self.EngPushButton.setObjectName(u"EngPushButton")
        self.EngPushButton.setGeometry(QRect(229, 190, 90, 74))
        self.EngPushButton.setAutoDefault(False)
        self.EngPushButton.setFlat(False)
        self.SocPushButton = QPushButton(SelectSubject)
        self.SocPushButton.setObjectName(u"SocPushButton")
        self.SocPushButton.setGeometry(QRect(365, 190, 90, 74))
        self.SocPushButton.setAutoDefault(False)
        self.SocPushButton.setFlat(False)
        self.SciPushButton = QPushButton(SelectSubject)
        self.SciPushButton.setObjectName(u"SciPushButton")
        self.SciPushButton.setGeometry(QRect(500, 190, 90, 74))
        self.SciPushButton.setAutoDefault(False)
        self.SciPushButton.setFlat(False)
        self.SelectSubjectlabel = QLabel(SelectSubject)
        self.SelectSubjectlabel.setObjectName(u"SelectSubjectlabel")
        self.SelectSubjectlabel.setGeometry(QRect(240, 100, 231, 51))
        font = QFont()
        font.setPointSize(27)
        self.SelectSubjectlabel.setFont(font)
        self.SelectSubjectlabel.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.MathPushButton, self.EngPushButton)
        QWidget.setTabOrder(self.EngPushButton, self.SocPushButton)
        QWidget.setTabOrder(self.SocPushButton, self.SciPushButton)

        self.retranslateUi(SelectSubject)

        QMetaObject.connectSlotsByName(SelectSubject)
    # setupUi

    def retranslateUi(self, SelectSubject):
        SelectSubject.setWindowTitle(QCoreApplication.translate("SelectSubject", u"WizardPage", None))
        self.MathPushButton.setText(QCoreApplication.translate("SelectSubject", u"Math", None))
        self.EngPushButton.setText(QCoreApplication.translate("SelectSubject", u"Eng", None))
        self.SocPushButton.setText(QCoreApplication.translate("SelectSubject", u"Soc", None))
        self.SciPushButton.setText(QCoreApplication.translate("SelectSubject", u"Sci", None))
        self.SelectSubjectlabel.setText(QCoreApplication.translate("SelectSubject", u"Select Subjects", None))
    # retranslateUi

