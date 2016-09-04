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
        MainWindow.resize(781, 438)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_requisition_tab = QtGui.QVBoxLayout()
        self.verticalLayout_requisition_tab.setObjectName(_fromUtf8("verticalLayout_requisition_tab"))
        self.verticalLayout_3.addLayout(self.verticalLayout_requisition_tab)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_contract_tab = QtGui.QVBoxLayout()
        self.verticalLayout_contract_tab.setObjectName(_fromUtf8("verticalLayout_contract_tab"))
        self.verticalLayout_4.addLayout(self.verticalLayout_contract_tab)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_acceptance_tab = QtGui.QVBoxLayout()
        self.verticalLayout_acceptance_tab.setObjectName(_fromUtf8("verticalLayout_acceptance_tab"))
        self.verticalLayout_6.addLayout(self.verticalLayout_acceptance_tab)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_printer_tab = QtGui.QVBoxLayout()
        self.verticalLayout_printer_tab.setObjectName(_fromUtf8("verticalLayout_printer_tab"))
        self.verticalLayout_8.addLayout(self.verticalLayout_printer_tab)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_inventory = QtGui.QHBoxLayout()
        self.horizontalLayout_inventory.setSpacing(0)
        self.horizontalLayout_inventory.setObjectName(_fromUtf8("horizontalLayout_inventory"))
        self.verticalLayout.addLayout(self.horizontalLayout_inventory)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "简·单", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "采购申请", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "合同管理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "入库报销", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "单据打印", None))
