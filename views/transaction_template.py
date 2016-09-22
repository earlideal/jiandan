# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaction_template.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(224, 78)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
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
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_contract_tab = QtGui.QVBoxLayout()
        self.verticalLayout_contract_tab.setObjectName(_fromUtf8("verticalLayout_contract_tab"))
        self.verticalLayout_4.addLayout(self.verticalLayout_contract_tab)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_acceptance_tab = QtGui.QVBoxLayout()
        self.verticalLayout_acceptance_tab.setObjectName(_fromUtf8("verticalLayout_acceptance_tab"))
        self.verticalLayout_6.addLayout(self.verticalLayout_acceptance_tab)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_inventory = QtGui.QHBoxLayout()
        self.horizontalLayout_inventory.setSpacing(0)
        self.horizontalLayout_inventory.setObjectName(_fromUtf8("horizontalLayout_inventory"))
        self.verticalLayout.addLayout(self.horizontalLayout_inventory)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "采购申请", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "合同管理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "入库报销", None))
