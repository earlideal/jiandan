# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from dashboard import DashboardWindow

if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('Source Han Sans medium', 12))
    # app.setFont(QtGui.QFont('trebuchet ms', 12))
    app.setStyle('plastique')
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
