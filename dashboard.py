# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from transaction import TransactionWidget
from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_back_home.clicked.connect(self.back_home)

        self.table_model = QtGui.QStandardItemModel()
        headers = [u'产品名称', u'型号规格', u'生产厂家', u'资产类型', u'单位', u'数量', u'原始报价',
                   u'报价币种', u'请购价格', u'请购金额', u'结算价格', u'结算金额']
        self.table_model.setHorizontalHeaderLabels(headers)
        self.ui.tableView.setModel(self.table_model)

        self.ui.summary_widget.hide()
        self.transaction_widget = TransactionWidget()
        self.ui.horizontalLayout_content.addWidget(self.transaction_widget)
        # 如果想要从布局中移除控件，必须在移除后再调用deleteLater方法，否则控件会自由浮动，但不会消失
        # self.ui.horizontalLayout_content.removeWidget(self.transaction_widget)
        # self.transaction_widget.deleteLater()

    def back_home(self):
        self.transaction_widget.hide()
        self.ui.summary_widget.show()
