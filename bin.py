from PyQt4 import QtGui

from dashboard_controller import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('book antiqua', 9))
    app.setStyle('windows')
    window = MainWindow()
    window.showMaximized()
    app.exec_()
