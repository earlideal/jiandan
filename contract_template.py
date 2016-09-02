# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contract_template.ui'
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
        Form.resize(613, 174)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_company_telephone = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_company_telephone.sizePolicy().hasHeightForWidth())
        self.lineEdit_company_telephone.setSizePolicy(sizePolicy)
        self.lineEdit_company_telephone.setReadOnly(True)
        self.lineEdit_company_telephone.setObjectName(_fromUtf8("lineEdit_company_telephone"))
        self.gridLayout.addWidget(self.lineEdit_company_telephone, 2, 5, 1, 1)
        self.comboBox_company = QtGui.QComboBox(self.groupBox)
        self.comboBox_company.setObjectName(_fromUtf8("comboBox_company"))
        self.gridLayout.addWidget(self.comboBox_company, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.lineEdit_contract_number = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_contract_number.setObjectName(_fromUtf8("lineEdit_contract_number"))
        self.gridLayout.addWidget(self.lineEdit_contract_number, 1, 1, 1, 1)
        self.doubleSpinBox_contract_amount = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_contract_amount.setObjectName(_fromUtf8("doubleSpinBox_contract_amount"))
        self.gridLayout.addWidget(self.doubleSpinBox_contract_amount, 1, 3, 1, 1)
        self.dateEdit_sign_date = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_sign_date.setObjectName(_fromUtf8("dateEdit_sign_date"))
        self.gridLayout.addWidget(self.dateEdit_sign_date, 1, 5, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_contract_name = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_contract_name.setObjectName(_fromUtf8("lineEdit_contract_name"))
        self.gridLayout.addWidget(self.lineEdit_contract_name, 0, 1, 1, 5)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_company_address = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_company_address.setReadOnly(True)
        self.lineEdit_company_address.setObjectName(_fromUtf8("lineEdit_company_address"))
        self.gridLayout.addWidget(self.lineEdit_company_address, 3, 1, 1, 4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 5, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_company_contact = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_company_contact.sizePolicy().hasHeightForWidth())
        self.lineEdit_company_contact.setSizePolicy(sizePolicy)
        self.lineEdit_company_contact.setMaxLength(12)
        self.lineEdit_company_contact.setReadOnly(True)
        self.lineEdit_company_contact.setObjectName(_fromUtf8("lineEdit_company_contact"))
        self.gridLayout.addWidget(self.lineEdit_company_contact, 2, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "合同信息", None))
        self.label_7.setText(_translate("Form", "联系电话", None))
        self.label_4.setText(_translate("Form", "签订日期", None))
        self.dateEdit_sign_date.setDisplayFormat(_translate("Form", "yyyy-M-d", None))
        self.label_3.setText(_translate("Form", "合同金额", None))
        self.label_5.setText(_translate("Form", "合同供方", None))
        self.lineEdit_contract_name.setText(_translate("Form", "测试用例合同名称随机", None))
        self.label_2.setText(_translate("Form", "合同编号", None))
        self.label.setText(_translate("Form", "合同名称", None))
        self.label_8.setText(_translate("Form", "联系地址", None))
        self.pushButton.setText(_translate("Form", "管理公司信息", None))
        self.label_6.setText(_translate("Form", "联系人", None))
