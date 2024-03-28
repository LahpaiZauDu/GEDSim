from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from login_ui import Ui_LoginWizardPage
from createnewuser_ui import Ui_CreateNewUserWizardPage
from selectsubject_ui import Ui_SelectSubject

# Base class for wizard pages


class BaseWizardPage(QWizardPage):
    def __init__(self):
        super().__init__()

    # Common setup logic (e.g., UI initialization)
    def setup_common_ui(self, ui_instance):
        self.ui = ui_instance
        self.ui.setupUi(self)

# Specific page classes


class MainPage(BaseWizardPage):
    def __init__(self):
        super().__init__()
        self.setup_common_ui(Ui_LoginWizardPage())

        # Connect button click signals to methods
        self.ui.LoginPushButton.clicked.connect(self.handle_action)
        self.ui.NewUserPushButton.clicked.connect(self.handle_action)

    def handle_action(self):
        sender_button = self.sender()
        if sender_button == self.ui.LoginPushButton:
            # User clicked "Login" button
            self.selectsubject = SelectSubject()
            wizard.addPage(self.selectsubject)
            wizard.setCurrentId(1)
        elif sender_button == self.ui.NewUserPushButton:
            # User clicked "New User" button
            self.newuser = CreateNewuser()
            wizard.addPage(self.newuser)
            wizard.setCurrentId(2)


class CreateNewuser(BaseWizardPage):
    def __init__(self):
        super().__init__()
        self.setup_common_ui(Ui_CreateNewUserWizardPage())


class SelectSubject(BaseWizardPage):
    def __init__(self):
        super().__init__()
        self.setup_common_ui(Ui_SelectSubject())


# Create the wizard and add pages
app = QApplication([])
app.setStyle("Fusion")
wizard = QWizard()
wizard.addPage(MainPage())
# Add other pages here...

# Show the wizard
wizard.show()
app.exec()
