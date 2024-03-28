# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QWizardPage)

class Ui_LoginWizardPage(object):
    def setupUi(self, LoginWizardPage):
        if not LoginWizardPage.objectName():
            LoginWizardPage.setObjectName(u"LoginWizardPage")
        LoginWizardPage.resize(648, 484)
        LoginWizardPage.setMinimumSize(QSize(648, 484))
        LoginWizardPage.setMaximumSize(QSize(648, 484))
        LoginWizardPage.setBaseSize(QSize(0, 0))
        LoginWizardPage.setFocusPolicy(Qt.ClickFocus)
        LoginWizardPage.setContextMenuPolicy(Qt.NoContextMenu)
        LoginWizardPage.setWindowOpacity(1.000000000000000)
        self.LoginPushButton = QPushButton(LoginWizardPage)
        self.LoginPushButton.setObjectName(u"LoginPushButton")
        self.LoginPushButton.setGeometry(QRect(220, 260, 100, 52))
        self.LoginPushButton.setMinimumSize(QSize(40, 40))
        self.LoginPushButton.setFocusPolicy(Qt.ClickFocus)
        self.StatusLabel = QLabel(LoginWizardPage)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setGeometry(QRect(260, 390, 151, 41))
        font = QFont()
        font.setPointSize(33)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setLineWidth(50)
        self.StatusLabel.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(LoginWizardPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 140, 191, 116))
        self.layoutWidget.setMinimumSize(QSize(40, 40))
        self.layoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UserIdLineEdit = QLineEdit(self.layoutWidget)
        self.UserIdLineEdit.setObjectName(u"UserIdLineEdit")
        self.UserIdLineEdit.setMinimumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(15)
        self.UserIdLineEdit.setFont(font1)
        self.UserIdLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.UserIdLineEdit.setAutoFillBackground(False)
        self.UserIdLineEdit.setInputMethodHints(Qt.ImhNone)
        self.UserIdLineEdit.setInputMask(u"")
        self.UserIdLineEdit.setMaxLength(6)
        self.UserIdLineEdit.setAlignment(Qt.AlignCenter)
        self.UserIdLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.UserIdLineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.UserIdLineEdit, 0, 0, 1, 1)

        self.PasswordLineEdit = QLineEdit(self.layoutWidget)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setMinimumSize(QSize(0, 40))
        self.PasswordLineEdit.setFont(font1)
        self.PasswordLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.PasswordLineEdit.setInputMask(u"")
        self.PasswordLineEdit.setMaxLength(6)
        self.PasswordLineEdit.setAlignment(Qt.AlignCenter)
        self.PasswordLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.PasswordLineEdit, 1, 0, 1, 1)

        self.NewUserPushButton = QPushButton(LoginWizardPage)
        self.NewUserPushButton.setObjectName(u"NewUserPushButton")
        self.NewUserPushButton.setGeometry(QRect(330, 260, 100, 52))
        self.NewUserPushButton.setMinimumSize(QSize(40, 40))
        self.NewUserPushButton.setFocusPolicy(Qt.ClickFocus)

        self.retranslateUi(LoginWizardPage)

        QMetaObject.connectSlotsByName(LoginWizardPage)
    # setupUi

    def retranslateUi(self, LoginWizardPage):
        LoginWizardPage.setWindowTitle(QCoreApplication.translate("LoginWizardPage", u"WizardPage", None))
        self.LoginPushButton.setText(QCoreApplication.translate("LoginWizardPage", u"Login", None))
        self.StatusLabel.setText(QCoreApplication.translate("LoginWizardPage", u"okay", None))
        self.UserIdLineEdit.setPlaceholderText(QCoreApplication.translate("LoginWizardPage", u"userid", None))
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("LoginWizardPage", u"password", None))
        self.NewUserPushButton.setText(QCoreApplication.translate("LoginWizardPage", u"New User", None))
    # retranslateUi

