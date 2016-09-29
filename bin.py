# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from dashboard import DashboardWindow

if __name__ == '__main__':
    app = QtGui.QApplication([])
    QtGui.QFontDatabase.addApplicationFont("resources/Ping Hei Text.ttf")
    app.setFont(QtGui.QFont('microsoft yahei', 10))
    app.setStyle('windowsvista')
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
