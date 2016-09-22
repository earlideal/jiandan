from PyQt4 import QtGui

from dashboard import DashboardWindow
from tables import win32word

if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    app.setStyle('windows')
    w = win32word.WordProcessor()
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
