from PyQt4 import QtGui

from dashboard import DashboardWindow

if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('book antiqua', 9))
    app.setStyle('windowsvista')
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
