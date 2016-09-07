# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import printer_template


class PrinterWindow(QtGui.QWidget):
    def __init__(self):
        super(PrinterWindow, self).__init__()
        self.ui = printer_template.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.print_qinggou_table)

    def print_qinggou_table(self):
        print "qinggou"
