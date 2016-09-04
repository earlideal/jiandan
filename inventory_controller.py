# -*- coding: utf-8 -*-
from functools import partial

from PyQt4 import QtGui

import editor_template
import inventory_template


class InventoryWindow(QtGui.QWidget):
    DOWN = 1
    UP = -1

    def __init__(self):
        super(InventoryWindow, self).__init__()
        self.ui = inventory_template.Ui_Form()
        self.ui.setupUi(self)

        self.model = QtGui.QStandardItemModel()
        headers = [u'产品名称', u'型号规格', u'单位', u'数量', u'预算单价', u'预算金额', u'经销商', u'结算单价', u'结算金额', u'资产类型']
        self.model.setHorizontalHeaderLabels(headers)
        self.ui.treeView.setModel(self.model)
        self.model.itemChanged.connect(self.on_item_changed)
        self.ui.treeView.setUniformRowHeights(True)
        self.ui.treeView.setAlternatingRowColors(True)
        self.ui.treeView.setAllColumnsShowFocus(True)

        self.ui.toolButton_append.clicked.connect(self._append_item)
        self.ui.toolButton_remove.clicked.connect(self._remove_item)
        self.ui.toolButton_export.clicked.connect(self._list_all_items)
        self.ui.toolButton_up.clicked.connect(partial(self._move_item, self.UP))
        self.ui.toolButton_down.clicked.connect(partial(self._move_item, self.DOWN))
        self.editor = EditorDialog()

    def _append_item(self):
        # if editor is a QWidget, use the following code to set window modal state
        # self.editor.setWindowModality(QtCore.Qt.ApplicationModal)
        if self.editor.exec_():
            single_row = []
            data = self.editor.take_data()
            for var in ['name', 'model', 'unit', 'quantity', 'price', 'amount']:
                single_row.append(QtGui.QStandardItem(data[var]))
                single_row[0].setCheckable(True)

            self.model.appendRow(single_row)

    def _remove_item(self):
        items = []
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            if item.checkState():
                items.append(item)
        for i in items:
            self.model.removeRow(i.row())

    def edit_item(self):
        pass

    def _move_item(self, direction):
        if direction not in (self.DOWN, self.UP):
            return

        model = self.model
        selection_model = self.ui.treeView.selectionModel()
        selected_rows = selection_model.selectedRows()
        if not selected_rows:
            return

        items = []
        indexes = sorted(selected_rows, key=lambda x: x.row(), reverse=(direction == self.DOWN))

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

    def on_item_changed(self, item):
        pass

    def _list_all_items(self):
        for i in xrange(self.model.rowCount()):
            for j in xrange(self.model.columnCount()):
                index = self.model.index(i, j)
                print unicode(self.model.itemFromIndex(index).text())


class EditorDialog(QtGui.QDialog):
    def __init__(self):
        # 注意：已经在设计窗体时将按钮信号和对话框的槽链接到一起了
        super(EditorDialog, self).__init__()
        self.ui = editor_template.Ui_Dialog()
        self.ui.setupUi(self)
        self.calculate_amount_money()
        self.ui.doubleSpinBox_budget_price.valueChanged.connect(self.calculate_amount_money)
        self.ui.doubleSpinBox_quantity.valueChanged.connect(self.calculate_amount_money)

    def calculate_amount_money(self):
        quantity_value = self.ui.doubleSpinBox_quantity.value()
        self.quantity = '%s' % quantity_value
        price_value = self.ui.doubleSpinBox_budget_price.value()
        self.price = '%0.2f' % price_value
        sum_value = quantity_value * price_value
        self.sum_text = '%0.2f' % sum_value
        self.ui.doubleSpinBox_budget_sum.setValue(sum_value)

    def take_data(self):
        quantity = self.quantity
        price = self.price
        amount = self.sum_text

        name = self.ui.lineEdit_name.text()
        model = self.ui.lineEdit_model.text()
        unit = self.ui.lineEdit_unit.text()

        manufacture = self.ui.lineEdit_manufacture.text()
        distributor = self.ui.lineEdit_distributor.text()
        description = self.ui.plainTextEdit_description.toPlainText()

        data = {}
        for varible in ['name', 'model', 'unit', 'quantity', 'price', 'amount', 'manufacture', 'distributor',
                        'description']:
            data[varible] = unicode(eval(varible))
        return data
