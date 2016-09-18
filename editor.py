# -*- coding: utf-8 -*-

import copy

from PyQt4 import QtGui

from model import Inventory
from views import editor_template


class EditorDialog(QtGui.QDialog):
    def __init__(self):
        super(EditorDialog, self).__init__()
        self.ui = editor_template.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.doubleSpinBox_quantity.valueChanged.connect(self._caculate_sum_money)
        self.ui.doubleSpinBox_acceptance_price.valueChanged.connect(self._caculate_sum_money)
        self.ui.doubleSpinBox_requisition_price.valueChanged.connect(self._caculate_sum_money)

    def _caculate_sum_money(self):
        quantity = self.ui.doubleSpinBox_quantity.value()
        price_req = self.ui.doubleSpinBox_requisition_price.value()
        self.ui.doubleSpinBox_requisition_sum.setValue(quantity * price_req)
        price_acc = self.ui.doubleSpinBox_acceptance_price.value()
        self.ui.doubleSpinBox_acceptance_sum.setValue(quantity * price_acc)

    def get_data(self):
        return self._update_model_from_view()

    def _update_model_from_view(self):
        self.name = unicode(self.ui.lineEdit_name.text())
        self.model = unicode(self.ui.lineEdit_model.text())
        self.manufacture = unicode(self.ui.lineEdit_manufacture.text())
        self.property_type = unicode(self.ui.comboBox_property_type.currentText())
        self.unit = unicode(self.ui.lineEdit_unit.text())
        self.quantity = self.ui.doubleSpinBox_quantity.value()
        self.quotation_price = self.ui.doubleSpinBox_quotation_price.value()
        self.quotation_currency = unicode(self.ui.comboBox_quotation_currency.currentText())
        self.requisition_price = self.ui.doubleSpinBox_requisition_price.value()
        self.requisition_sum = self.ui.doubleSpinBox_requisition_sum.value()
        self.acceptance_price = self.ui.doubleSpinBox_acceptance_price.value()
        self.acceptance_sum = self.ui.doubleSpinBox_acceptance_sum.value()
        self.description = unicode(self.ui.plainTextEdit.toPlainText())
        items = copy.deepcopy(self.__dict__)
        items.pop('ui')

        keys = items.keys()
        inventory = Inventory()
        for key in keys:
            if hasattr(inventory, key):
                setattr(inventory, key, items[key])
            else:
                print u'未发现键值：', key
        return items
