# -*- coding: utf-8 -*-
from functools import partial

from PyQt4 import QtGui

from editor import EditorDialog
from views import inventory_template


class InventoryWindow(QtGui.QWidget):
    DOWN = 1
    UP = -1

    def __init__(self):
        super(InventoryWindow, self).__init__()
        self.ui = inventory_template.Ui_Form()
        self.ui.setupUi(self)

        self.table_model = QtGui.QStandardItemModel()
        headers = [u'产品名称', u'型号规格', u'生产厂家', u'资产类型', u'单位', u'数量', u'原始报价',
                   u'报价币种', u'请购价格', u'请购金额', u'结算价格', u'结算金额']
        self.keys = ['name', 'model', 'manufacture', 'property_type', 'unit', 'quantity', 'quotation_price',
                     'quotation_currency', 'requisition_price', 'requisition_sum', 'acceptance_price', 'acceptance_sum']
        self.table_model.setHorizontalHeaderLabels(headers)

        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.setAlternatingRowColors(True)

        self.ui.toolButton_append.clicked.connect(self._append_item)
        self.ui.toolButton_remove.clicked.connect(self._remove_item)
        self.ui.toolButton_up.clicked.connect(partial(self._move_item, self.UP))
        self.ui.toolButton_down.clicked.connect(partial(self._move_item, self.DOWN))

        self.ui.doubleSpinBox_acceptance_total.editingFinished.connect(partial(self._recaculate_money, 0))
        self.ui.doubleSpinBox_requisition_total.editingFinished.connect(partial(self._recaculate_money, 1))

        self.inventories = []

        self.editor = EditorDialog()

    def _append_item(self):
        # if editor is a QWidget, use the following code to set window modal state
        # self.editor.setWindowModality(QtCore.Qt.ApplicationModal)
        self.editor = EditorDialog()
        if self.editor.exec_():
            data = self.editor.get_data()
            self.inventories.append(data)
            row = []

            for k in self.keys:
                x = data[k]
                if not isinstance(x, unicode):
                    x = "%.2f" % x
                row.append(QtGui.QStandardItem(x))

                # 设置首列为可选择
                # row[0].setCheckable(True)

            self.table_model.appendRow(row)

            # 让表格的列宽自适应内容变化
            # self.ui.tableView.resizeColumnsToContents()

            # 获取表格中某一格内容的方法
            self.table_model.item(0, 6).text()

    def _remove_item(self):
        items = []
        for i in range(self.table_model.rowCount()):
            item = self.table_model.item(i)
            if item.checkState():
                items.append(item)
        for i in items:
            self.table_model.removeRow(i.row())

    def _move_item(self, direction):
        if direction not in (self.DOWN, self.UP):
            return

        selection_model = self.ui.tableView.selectionModel()
        selected_rows = selection_model.selectedRows()
        if not selected_rows:
            return

        items = []
        indexes = sorted(selected_rows, key=lambda x: x.row(), reverse=(direction == self.DOWN))

        model = self.table_model
        for index in indexes:
            item = model.itemFromIndex(index)
            items.append(item)
            row_num = index.row()
            new_row = row_num + direction
            if not (0 <= new_row < model.rowCount()):
                continue

            rowItems = model.takeRow(row_num)
            model.insertRow(new_row, rowItems)

        selection_model.clear()
        for item in items:
            selection_model.select(item.index(), selection_model.Select | selection_model.Rows)

    def _recaculate_money(self, req):
        if len(self.inventories) == 0:
            return
        if req:
            total = self.ui.doubleSpinBox_requisition_total.value()
            price_str = 'requisition_price'
            sum_str = 'requisition_sum'
        else:
            total = self.ui.doubleSpinBox_acceptance_total.value()
            price_str = 'acceptance_price'
            sum_str = 'acceptance_sum'
        row_number = len(self.inventories)
        sum = 0
        sum_list = []
        sum_ratio_list = []
        recaculated_sum_list = []
        for data_dict in self.inventories:
            quantity = data_dict['quantity']
            quotation_price = data_dict['quotation_price']
            quotation_sum = quantity * quotation_price
            sum_list.append(quotation_sum)
            sum += quotation_sum

        for s in sum_list:
            ratio = s / sum
            sum_ratio_list.append(ratio)  # 注意这个地方的除法是否会只是取整
            recaculated_sum_list.append(ratio * total)

        # 更新tableView的数据模型相关位置的数据
        ind = self.keys.index(price_str)
        for i in xrange(len(self.inventories)):
            self.inventories[i][sum_str] = recaculated_sum_list[i]
            self.inventories[i][price_str] = recaculated_sum_list[i] / self.inventories[i]['quantity']
            self.table_model.item(i, ind).setText('%.4f' % (self.inventories[i][price_str]))
            self.table_model.item(i, ind + 1).setText('%.4f' % (self.inventories[i][sum_str]))
            # TODO 需要建立通过model更新界面的模型
