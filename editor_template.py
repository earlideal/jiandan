# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_template.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(786, 360)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.doubleSpinBox_quantity = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_quantity.setObjectName(_fromUtf8("doubleSpinBox_quantity"))
        self.gridLayout.addWidget(self.doubleSpinBox_quantity, 1, 3, 1, 1)
        self.lineEdit_model = QtGui.QLineEdit(Dialog)
        self.lineEdit_model.setObjectName(_fromUtf8("lineEdit_model"))
        self.gridLayout.addWidget(self.lineEdit_model, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)
        self.lineEdit_unit = QtGui.QLineEdit(Dialog)
        self.lineEdit_unit.setObjectName(_fromUtf8("lineEdit_unit"))
        self.gridLayout.addWidget(self.lineEdit_unit, 1, 1, 1, 1)
        self.doubleSpinBox_budget_sum = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_budget_sum.setObjectName(_fromUtf8("doubleSpinBox_budget_sum"))
        self.gridLayout.addWidget(self.doubleSpinBox_budget_sum, 1, 7, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.doubleSpinBox_budget_price = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_budget_price.setObjectName(_fromUtf8("doubleSpinBox_budget_price"))
        self.gridLayout.addWidget(self.doubleSpinBox_budget_price, 1, 5, 1, 1)
        self.lineEdit_manufacture = QtGui.QLineEdit(Dialog)
        self.lineEdit_manufacture.setObjectName(_fromUtf8("lineEdit_manufacture"))
        self.gridLayout.addWidget(self.lineEdit_manufacture, 0, 5, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 6, 1, 1)
        self.lineEdit_distributor = QtGui.QLineEdit(Dialog)
        self.lineEdit_distributor.setObjectName(_fromUtf8("lineEdit_distributor"))
        self.gridLayout.addWidget(self.lineEdit_distributor, 0, 7, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox_acceptance_price = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_acceptance_price.setObjectName(_fromUtf8("doubleSpinBox_acceptance_price"))
        self.gridLayout.addWidget(self.doubleSpinBox_acceptance_price, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_name = QtGui.QLineEdit(Dialog)
        self.lineEdit_name.setText(_fromUtf8(""))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.doubleSpinBox_acceptance_sum = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_acceptance_sum.setObjectName(_fromUtf8("doubleSpinBox_acceptance_sum"))
        self.gridLayout.addWidget(self.doubleSpinBox_acceptance_sum, 2, 3, 1, 1)
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.comboBox_property_type = QtGui.QComboBox(Dialog)
        self.comboBox_property_type.setObjectName(_fromUtf8("comboBox_property_type"))
        self.gridLayout.addWidget(self.comboBox_property_type, 2, 5, 1, 1)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.plainTextEdit_description = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_description.setObjectName(_fromUtf8("plainTextEdit_description"))
        self.verticalLayout.addWidget(self.plainTextEdit_description)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_name, self.lineEdit_model)
        Dialog.setTabOrder(self.lineEdit_model, self.lineEdit_manufacture)
        Dialog.setTabOrder(self.lineEdit_manufacture, self.lineEdit_distributor)
        Dialog.setTabOrder(self.lineEdit_distributor, self.lineEdit_unit)
        Dialog.setTabOrder(self.lineEdit_unit, self.doubleSpinBox_quantity)
        Dialog.setTabOrder(self.doubleSpinBox_quantity, self.doubleSpinBox_budget_price)
        Dialog.setTabOrder(self.doubleSpinBox_budget_price, self.doubleSpinBox_budget_sum)
        Dialog.setTabOrder(self.doubleSpinBox_budget_sum, self.doubleSpinBox_acceptance_price)
        Dialog.setTabOrder(self.doubleSpinBox_acceptance_price, self.doubleSpinBox_acceptance_sum)
        Dialog.setTabOrder(self.doubleSpinBox_acceptance_sum, self.comboBox_property_type)
        Dialog.setTabOrder(self.comboBox_property_type, self.plainTextEdit_description)
        Dialog.setTabOrder(self.plainTextEdit_description, self.pushButton_ok)
        Dialog.setTabOrder(self.pushButton_ok, self.pushButton_cancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "预算价格", None))
        self.label_8.setText(_translate("Dialog", "预算金额", None))
        self.label_3.setText(_translate("Dialog", "计价单位", None))
        self.label_6.setText(_translate("Dialog", "经销商", None))
        self.label_7.setText(_translate("Dialog", "生产厂家", None))
        self.label.setText(_translate("Dialog", "产品名称", None))
        self.label_2.setText(_translate("Dialog", "型号规格", None))
        self.label_4.setText(_translate("Dialog", "数量", None))
        self.label_13.setText(_translate("Dialog", "结算金额", None))
        self.label_10.setText(_translate("Dialog", "结算价格", None))
        self.label_9.setText(_translate("Dialog", "资产类型", None))
        self.label_12.setText(_translate("Dialog", "设备参数描述（用于固定资产设备卡）：", None))
        self.pushButton_ok.setText(_translate("Dialog", "确认", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))