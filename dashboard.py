# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from transaction import TransactionWidget
from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)

        self.transaction_widget = TransactionWidget()
        # self.ui.horizontalLayout_content.addWidget(self.transaction_widget)
        # 如果想要从布局中移除控件，必须在移除后再调用deleteLater方法，否则控件会自由浮动，但不会消失
        # self.ui.horizontalLayout_content.removeWidget(self.transaction_widget)
        # self.transaction_widget.deleteLater()
