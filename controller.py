# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import model
import requisition_template


class RequisitionWindow(QtGui.QWidget):
    def __init__(self):
        super(RequisitionWindow, self).__init__()
        self.ui = requisition_template.Ui_Form()
        self.ui.setupUi(self)
        self.requisition = model.PurchaseRequisition()
        self._update_model()

    def _update_model(self):
        self.requisition.applicant = self.ui.comboBox_applicant.currentText()
        self.requisition.add()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('Trebuchet MS', 9))
    w = RequisitionWindow()
    w.show()
    app.exec_()
