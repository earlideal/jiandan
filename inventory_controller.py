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
        headers = [u'产品名称', u'型号规格', u'生产厂家', u'资产类型', u'单位', u'数量', u'原始报价',
                   u'报价币种', u'请购价格', u'请购金额', u'结算价格', u'结算金额']
        self.model.setHorizontalHeaderLabels(headers)
        self.ui.tableView.setModel(self.model)
        self.model.itemChanged.connect(self.on_item_changed)
        # self.ui.treeView.setUniformRowHeights(True)
        self.ui.tableView.setAlternatingRowColors(True)
        # self.ui.treeView.setAllColumnsShowFocus(True)

        self.ui.toolButton_append.clicked.connect(self._append_item)
        self.ui.toolButton_remove.clicked.connect(self._remove_item)
        self.ui.toolButton_export.clicked.connect(self._list_all_items)
        self.ui.toolButton_up.clicked.connect(partial(self._move_item, self.UP))
        self.ui.toolButton_down.clicked.connect(
            partial(self._move_item, self.DOWN))

        self.editor = EditorDialog()

    def _append_item(self):
        # if editor is a QWidget, use the following code to set window modal state
        # self.editor.setWindowModality(QtCore.Qt.ApplicationModal)
        if self.editor.exec_():
            single_row = []
            data = self.editor.get_editor_data()
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
        selection_model = self.ui.tableView.selectionModel()
        selected_rows = selection_model.selectedRows()
        if not selected_rows:
            return

        items = []
        indexes = sorted(selected_rows, key=lambda x: x.row(),
                         reverse=(direction == self.DOWN))

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

    def get_editor_data(self):
        pass
