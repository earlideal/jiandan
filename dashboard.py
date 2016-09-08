from PyQt4 import QtGui

from views import dashboard_template


class DashboardWindow(QtGui.QMainWindow):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('book antiqua', 9))
    app.setStyle('windows')
    window = DashboardWindow()
    window.showMaximized()
    app.exec_()
