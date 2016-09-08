from PyQt4 import QtGui

from views import acceptance_template


class AcceptanceWindow(QtGui.QWidget):
    def __init__(self):
        super(AcceptanceWindow, self).__init__()
        self.ui = acceptance_template.Ui_Form()
        self.ui.setupUi(self)
