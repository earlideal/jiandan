# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory_template.ui'
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
        Form.resize(443, 276)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_import = QtGui.QToolButton(Form)
        self.toolButton_import.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_import.setObjectName(_fromUtf8("toolButton_import"))
        self.horizontalLayout.addWidget(self.toolButton_import)
        self.toolButton_export = QtGui.QToolButton(Form)
        self.toolButton_export.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_export.setObjectName(_fromUtf8("toolButton_export"))
        self.horizontalLayout.addWidget(self.toolButton_export)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.toolButton_append = QtGui.QToolButton(Form)
        self.toolButton_append.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_append.setObjectName(_fromUtf8("toolButton_append"))
        self.horizontalLayout.addWidget(self.toolButton_append)
        self.toolButton_remove = QtGui.QToolButton(Form)
        self.toolButton_remove.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_remove.setObjectName(_fromUtf8("toolButton_remove"))
        self.horizontalLayout.addWidget(self.toolButton_remove)
        self.toolButton_edit = QtGui.QToolButton(Form)
        self.toolButton_edit.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_edit.setObjectName(_fromUtf8("toolButton_edit"))
        self.horizontalLayout.addWidget(self.toolButton_edit)
        self.toolButton_up = QtGui.QToolButton(Form)
        self.toolButton_up.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_up.setObjectName(_fromUtf8("toolButton_up"))
        self.horizontalLayout.addWidget(self.toolButton_up)
        self.toolButton_down = QtGui.QToolButton(Form)
        self.toolButton_down.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_down.setObjectName(_fromUtf8("toolButton_down"))
        self.horizontalLayout.addWidget(self.toolButton_down)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.doubleSpinBox_requisition_total = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_requisition_total.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_requisition_total.setSizePolicy(sizePolicy)
        self.doubleSpinBox_requisition_total.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_requisition_total.setObjectName(_fromUtf8("doubleSpinBox_requisition_total"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_requisition_total)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.doubleSpinBox_acceptance_total = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_acceptance_total.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_acceptance_total.setSizePolicy(sizePolicy)
        self.doubleSpinBox_acceptance_total.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_acceptance_total.setObjectName(_fromUtf8("doubleSpinBox_acceptance_total"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_acceptance_total)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton_import.setText(_translate("Form", "导入", None))
        self.toolButton_export.setText(_translate("Form", "导出", None))
        self.toolButton_append.setText(_translate("Form", "添加", None))
        self.toolButton_remove.setText(_translate("Form", "删除", None))
        self.toolButton_edit.setText(_translate("Form", "编辑", None))
        self.toolButton_up.setText(_translate("Form", "上移", None))
        self.toolButton_down.setText(_translate("Form", "下移", None))
        self.label.setText(_translate("Form", "请购总计：", None))
        self.label_2.setText(_translate("Form", "结算总计：", None))
