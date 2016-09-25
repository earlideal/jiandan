# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import model
from sheets_handler import PrintDialog
from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont(u'方正启体简体', 28))
        self.ui.toolButton_home.clicked.connect(self.go_home)
        self.ui.toolButton_print.clicked.connect(self.show_print_dialog)

        # headers = [u'事务流水', u'请购标题', u'合同管理', u'经办人', u'创建时间', u'修改时间']
        self.table_model = QtGui.QStandardItemModel()
        # self.table_model.setHorizontalHeaderLabels(headers)
        self.ui.tableView.setModel(self.table_model)

        # self.ui.summary_widget.hide()
        # self.transaction_widget = TransactionWidget()
        # self.ui.horizontalLayout_content.addWidget(self.transaction_widget)
        # 如果想要从布局中移除控件，必须在移除后再调用deleteLater方法，否则控件会自由浮动，但不会消失
        # self.ui.horizontalLayout_content.removeWidget(self.transaction_widget)
        # self.transaction_widget.deleteLater()

    def go_home(self):
        # if self.transaction_widget.isHidden():
        #     self.transaction_widget.show()
        #     self.ui.summary_widget.hide()
        # else:
        #     self.transaction_widget.hide()
        #     self.ui.summary_widget.show()
        self.list_all_transactions()

    def list_all_transactions(self):
        self.table_model.clear()
        headers = [u'事务流水', u'请购标题', u'合同管理', u'经办人', u'创建时间', u'修改时间']
        self.table_model.setHorizontalHeaderLabels(headers)
        trans = model.session.query(model.Transaction).all()
        for t in trans:
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
            self.ui.tableView.resizeColumnsToContents()

    def show_print_dialog(self):
        dialog = PrintDialog()
        dialog.exec_()
