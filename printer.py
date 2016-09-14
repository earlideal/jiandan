# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from tables import word
from views import printer_template


class PrinterWidget(QtGui.QWidget):
    def __init__(self):
        super(PrinterWidget, self).__init__()
        self.ui = printer_template.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.print_qinggou_table)

    def print_qinggou_table(self):
        w = word.WordProcessor()
