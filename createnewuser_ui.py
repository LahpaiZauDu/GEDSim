# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createnewuser.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QWizardPage)

class Ui_CreateNewUserWizardPage(object):
    def setupUi(self, CreateNewUserWizardPage):
        if not CreateNewUserWizardPage.objectName():
            CreateNewUserWizardPage.setObjectName(u"CreateNewUserWizardPage")
        CreateNewUserWizardPage.resize(640, 480)
        CreateNewUserWizardPage.setMinimumSize(QSize(640, 480))
        CreateNewUserWizardPage.setMaximumSize(QSize(640, 480))
        self.layoutWidget = QWidget(CreateNewUserWizardPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 190, 296, 42))
        self.layoutWidget.setMinimumSize(QSize(40, 40))
        self.layoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.UserIdLineEdit = QLineEdit(self.layoutWidget)
        self.UserIdLineEdit.setObjectName(u"UserIdLineEdit")
        self.UserIdLineEdit.setMinimumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(15)
        self.UserIdLineEdit.setFont(font)
        self.UserIdLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.UserIdLineEdit.setAutoFillBackground(False)
        self.UserIdLineEdit.setInputMethodHints(Qt.ImhNone)
        self.UserIdLineEdit.setInputMask(u"")
        self.UserIdLineEdit.setMaxLength(6)
        self.UserIdLineEdit.setAlignment(Qt.AlignCenter)
        self.UserIdLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.UserIdLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.UserIdLineEdit)

        self.PasswordLineEdit = QLineEdit(self.layoutWidget)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setMinimumSize(QSize(0, 40))
        self.PasswordLineEdit.setFont(font)
        self.PasswordLineEdit.setFocusPolicy(Qt.ClickFocus)
        self.PasswordLineEdit.setInputMask(u"")
        self.PasswordLineEdit.setMaxLength(6)
        self.PasswordLineEdit.setAlignment(Qt.AlignCenter)
        self.PasswordLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout.addWidget(self.PasswordLineEdit)

        self.CreatePushButton = QPushButton(CreateNewUserWizardPage)
        self.CreatePushButton.setObjectName(u"CreatePushButton")
        self.CreatePushButton.setGeometry(QRect(270, 260, 100, 52))
        self.CreatePushButton.setMinimumSize(QSize(40, 40))
        self.CreatePushButton.setFocusPolicy(Qt.ClickFocus)
        self.StatusLabel = QLabel(CreateNewUserWizardPage)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setGeometry(QRect(160, 100, 311, 41))
        font1 = QFont()
        font1.setPointSize(33)
        self.StatusLabel.setFont(font1)
        self.StatusLabel.setLineWidth(50)
        self.StatusLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(CreateNewUserWizardPage)

        QMetaObject.connectSlotsByName(CreateNewUserWizardPage)
    # setupUi

    def retranslateUi(self, CreateNewUserWizardPage):
        CreateNewUserWizardPage.setWindowTitle(QCoreApplication.translate("CreateNewUserWizardPage", u"WizardPage", None))
        self.UserIdLineEdit.setPlaceholderText(QCoreApplication.translate("CreateNewUserWizardPage", u"userid", None))
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("CreateNewUserWizardPage", u"password", None))
        self.CreatePushButton.setText(QCoreApplication.translate("CreateNewUserWizardPage", u"Create", None))
        self.StatusLabel.setText(QCoreApplication.translate("CreateNewUserWizardPage", u"Create New User", None))
    # retranslateUi

