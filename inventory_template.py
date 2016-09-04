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
        Form.resize(847, 468)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
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
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.toolButton_import = QtGui.QToolButton(Form)
        self.toolButton_import.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_import.setObjectName(_fromUtf8("toolButton_import"))
        self.horizontalLayout.addWidget(self.toolButton_import)
        self.toolButton_export = QtGui.QToolButton(Form)
        self.toolButton_export.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_export.setObjectName(_fromUtf8("toolButton_export"))
        self.horizontalLayout.addWidget(self.toolButton_export)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeView = QtGui.QTreeView(Form)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.horizontalLayout_2.addWidget(self.treeView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton_append.setText(_translate("Form", "添加", None))
        self.toolButton_remove.setText(_translate("Form", "删除", None))
        self.toolButton_edit.setText(_translate("Form", "编辑", None))
        self.toolButton_up.setText(_translate("Form", "上移", None))
        self.toolButton_down.setText(_translate("Form", "下移", None))
        self.toolButton_import.setText(_translate("Form", "导入", None))
        self.toolButton_export.setText(_translate("Form", "导出", None))
