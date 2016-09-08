from PyQt4 import QtGui

from controller.dashboard_controller import DashboardWindow

if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('book antiqua', 9))
    app.setStyle('windows')
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
