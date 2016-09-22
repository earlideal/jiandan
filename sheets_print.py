# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui

from views import sheets_print_template


class PrintDialog(QtGui.QDialog):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.ui = sheets_print_template.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toolButton_generate.clicked.connect(self._generate_sheets_list)
        self.sheets_name_zh = [u'请购单', u'采购申请评审表', u'采购合同评审表', u'检验单', u'仪器设备验收单', u'直发单', u'设备卡']
        self.sheets_name_en = ['REQUISITION_SHEET', 'REQUISITION_REVIEW_TABLE', 'CONTRACT_REVIEW_TABLE',
                               'VERIFICATION_SHEET', 'VERIFICATION_REVIEW_TABLE', 'LADING_BILL_SHEET', 'FACILITY_SHEET']

    def _generate_sheets_list(self):
        temp = (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(8)))).upper()
        os.mkdir(temp)
        path = os.path.abspath(temp)
        x = self.ui.verticalLayout_sheets
        while x.count():
            print x.count()
            w = x.takeAt(0)
            while w.count():
                y = w.children[0]
                w.removeWidget(y)
                y.deleteLater()
            w.deleteLater()

        for s in self.sheets_name_zh:
            self._generate_on_print_numbers(s)

    def _generate_on_print_numbers(self, title_text):
        label_req = QtGui.QLabel()
        label_req.setText(title_text)
        numbered_buttons = []
        for i in xrange(1, 3):
            toolButton = QtGui.QToolButton()
            font = QtGui.QFont()
            font.setUnderline(True)
            toolButton.setFont(font)
            toolButton.setAutoRaise(True)
            toolButton.setText(str(i))
            numbered_buttons.append(toolButton)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(label_req)
        for x in numbered_buttons:
            hbox.addWidget(x)
            x.clicked.connect(self.print_relevant_file)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        hbox.addItem(spacerItem)
        self.ui.verticalLayout_sheets.addLayout(hbox)

    def print_relevant_file(self):
        print unicode(self.sender().text()) + u'做了点击动作。'


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    app.setStyle('windowsvista')
    dialog = PrintDialog()
    dialog.show()
    app.exec_()
