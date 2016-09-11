# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import model
from transaction import TransactionWidget
from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_back_home.clicked.connect(self.back_home)

        headers = [u'事务流水', u'请购标题', u'请购总额', u'合同管理', u'入库报销', u'报销结算', u'经办人', u'创建时间', u'修改时间']
        self.table_model = QtGui.QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(headers)
        self.ui.tableView.setModel(self.table_model)

        self.ui.summary_widget.hide()
        self.transaction_widget = TransactionWidget()
        self.ui.horizontalLayout_content.addWidget(self.transaction_widget)
        # 如果想要从布局中移除控件，必须在移除后再调用deleteLater方法，否则控件会自由浮动，但不会消失
        # self.ui.horizontalLayout_content.removeWidget(self.transaction_widget)
        # self.transaction_widget.deleteLater()
        self.list_all_transactions()

    def back_home(self):
        if self.transaction_widget.isHidden():
            self.transaction_widget.show()
            self.ui.summary_widget.hide()
        else:
            self.transaction_widget.hide()
            self.ui.summary_widget.show()

    def list_all_transactions(self):
        trans = model.session.query(model.Transaction).all()
        for t in trans:
            # headers = [u'事务流水', u'请购标题', u'请购总额', u'合同管理', u'入库检验', u'报销结算', u'经办人', u'创建时间', u'修改时间']
            headers = [u'事务流水', u'请购标题', u'合同管理', u'经办人', u'创建时间', u'修改时间']
            keys = ['swiftcode', 'title', 'contract', 'applicant', 'createdtime', 'modifiedtime']
            req = model.session.query(model.Requisition).filter_by(id=t.requisition_id).first()
            cont = model.session.query(model.Contract).filter_by(id=t.contract_id).first()
            swiftcode = t.swift_code
            title = req.title
            contract = u'合同未录入'
            if not cont is None:
                contract = cont.name

            applicant = req.applicant.name
            createdtime = t.created_time.strftime("%Y-%m-%d %H:%M:%S")
            modifiedtime = t.modified_time.strftime("%Y-%m-%d %H:%M:%S")

            row = []
            for k in keys:
                item = QtGui.QStandardItem(eval(k))
                row.append(item)
            self.table_model.appendRow(row)
