# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from views import printer_template


class PrinterWidget(QtGui.QWidget):
    def __init__(self):
        super(PrinterWidget, self).__init__()
        self.ui = printer_template.Ui_Form()
        self.ui.setupUi(self)

        self.label_req = QtGui.QLabel()
        self.label_req.setText(u'请购单')

        on_printed_toolbuttons = []
        for i in xrange(1, 3):
            toolButton = QtGui.QToolButton()
            font = QtGui.QFont()
            font.setUnderline(True)
            toolButton.setFont(font)
            toolButton.setAutoRaise(True)
            toolButton.setText(str(i))
            on_printed_toolbuttons.append(toolButton)

        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.label_req)
        for x in on_printed_toolbuttons:
            self.hbox.addWidget(x)
            x.clicked.connect(self.print_relevant_file)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hbox.addItem(spacerItem)
        self.ui.horizontalLayout.addLayout(self.hbox)

    def print_relevant_file(self):
        print self.sender().text()
