from PyQt4 import QtGui

from transaction import TransactionWidget
from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)

        self.transaction_widget = TransactionWidget()
        self.ui.horizontalLayout_content.addWidget(self.transaction_widget)
