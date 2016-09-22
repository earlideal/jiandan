from PyQt4 import QtGui

import untitled


class TestWindow(QtGui.QWidget):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.ui = untitled.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.remove_layout)

    def remove_layout(self):
        print 'remove'
        print isinstance(self.ui.pushButton_2, QtGui.QWidget)
        print isinstance(self.ui.horizontalLayout, QtGui.QLayout)
        # self.ui.verticalLayout.removeItem(self.ui.horizontalLayout)
        # self.ui.horizontalLayout.deleteLater()
        self.ui.verticalLayout.removeWidget(self.ui.pushButton_2)
        self.ui.pushButton_2.deleteLater()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    app.setStyle('windowsvista')
    window = TestWindow()
    window.show()
    app.exec_()
