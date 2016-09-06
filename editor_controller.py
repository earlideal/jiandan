# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import editor_template


class EditorDialog(QtGui.QDialog):
    def __init__(self):
        super(EditorDialog, self).__init__()
        self.ui = editor_template.Ui_Dialog()
        self.ui.setupUi(self)
        self._update_model_from_view()

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
        print self.__dict__


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    window = EditorDialog()
    window.show()
    app.exec_()
