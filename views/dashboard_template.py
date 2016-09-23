# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_template.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(439, 163)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_home = QtGui.QToolButton(self.centralwidget)
        self.toolButton_home.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_home.setFont(font)
        self.toolButton_home.setAutoRaise(True)
        self.toolButton_home.setObjectName(_fromUtf8("toolButton_home"))
        self.horizontalLayout.addWidget(self.toolButton_home)
        self.toolButton_new_trans = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_new_trans.sizePolicy().hasHeightForWidth())
        self.toolButton_new_trans.setSizePolicy(sizePolicy)
        self.toolButton_new_trans.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_new_trans.setFont(font)
        self.toolButton_new_trans.setAutoRaise(True)
        self.toolButton_new_trans.setObjectName(_fromUtf8("toolButton_new_trans"))
        self.horizontalLayout.addWidget(self.toolButton_new_trans)
        self.toolButton_save_trans = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_save_trans.sizePolicy().hasHeightForWidth())
        self.toolButton_save_trans.setSizePolicy(sizePolicy)
        self.toolButton_save_trans.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_save_trans.setFont(font)
        self.toolButton_save_trans.setAutoRaise(True)
        self.toolButton_save_trans.setObjectName(_fromUtf8("toolButton_save_trans"))
        self.horizontalLayout.addWidget(self.toolButton_save_trans)
        self.toolButton_print = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_print.sizePolicy().hasHeightForWidth())
        self.toolButton_print.setSizePolicy(sizePolicy)
        self.toolButton_print.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_print.setFont(font)
        self.toolButton_print.setAutoRaise(True)
        self.toolButton_print.setObjectName(_fromUtf8("toolButton_print"))
        self.horizontalLayout.addWidget(self.toolButton_print)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_content = QtGui.QHBoxLayout()
        self.horizontalLayout_content.setObjectName(_fromUtf8("horizontalLayout_content"))
        self.summary_widget = QtGui.QWidget(self.centralwidget)
        self.summary_widget.setObjectName(_fromUtf8("summary_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.summary_widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableView = QtGui.QTableView(self.summary_widget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_content.addWidget(self.summary_widget)
        self.verticalLayout.addLayout(self.horizontalLayout_content)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "简·单", None))
        self.toolButton_home.setText(_translate("MainWindow", "首页", None))
        self.toolButton_new_trans.setText(_translate("MainWindow", "新建事务", None))
        self.toolButton_save_trans.setText(_translate("MainWindow", "保存事务", None))
        self.toolButton_print.setText(_translate("MainWindow", "打印事务", None))
