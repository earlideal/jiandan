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
        # os.mkdir(temp)
        path = os.path.abspath(temp)

        # frame.children()仅仅列出来最基础一层布局，不会列出来子布局
        # 想要列出子布局，必须用子布局的父级进行枚举，但这种方式不能枚举出子widget
        for child in self.ui.frame.children():
            if isinstance(child, QtGui.QWidget):
                self.ui.verticalLayout_sheets.removeWidget(child)
                child.deleteLater()
        for child in self.ui.verticalLayout_sheets.children():
            self.ui.verticalLayout_sheets.removeItem(child)

        for s in self.sheets_name_zh:
            self._generate_on_print_numbers(s)

    def _generate_on_print_numbers(self, title_text):
        label_req = QtGui.QLabel()
        label_req.setText(title_text)
        numbered_buttons = []
        for i in xrange(1, 10):
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
    app.setStyle('windows')
    dialog = PrintDialog()
    dialog.show()
    app.exec_()
