# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import model
import requisition_template
from model import session


class RequisitionWindow(QtGui.QWidget):
    def __init__(self):
        super(RequisitionWindow, self).__init__()
        self.ui = requisition_template.Ui_Form()
        self.ui.setupUi(self)
        self.staff = model.Person()
        self._update_model()

    def _update_model(self):
        staffs = session.query(model.Person).all()
        for i in xrange(len(staffs)):
            print staffs[i].name, staffs[i].id


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('Trebuchet MS', 9))
    window = RequisitionWindow()
    window.show()
    app.exec_()
