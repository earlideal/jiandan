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
        Form.resize(1031, 143)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_company = QtGui.QComboBox(Form)
        self.comboBox_company.setObjectName(_fromUtf8("comboBox_company"))
        self.gridLayout.addWidget(self.comboBox_company, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.lineEdit_company_contact = QtGui.QLineEdit(Form)
        self.lineEdit_company_contact.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_company_contact.sizePolicy().hasHeightForWidth())
        self.lineEdit_company_contact.setSizePolicy(sizePolicy)
        self.lineEdit_company_contact.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_company_contact.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_company_contact.setMaxLength(12)
        self.lineEdit_company_contact.setReadOnly(True)
        self.lineEdit_company_contact.setObjectName(_fromUtf8("lineEdit_company_contact"))
        self.gridLayout.addWidget(self.lineEdit_company_contact, 1, 3, 1, 1)
        self.lineEdit_company_address = QtGui.QLineEdit(Form)
        self.lineEdit_company_address.setEnabled(False)
        self.lineEdit_company_address.setReadOnly(True)
        self.lineEdit_company_address.setObjectName(_fromUtf8("lineEdit_company_address"))
        self.gridLayout.addWidget(self.lineEdit_company_address, 1, 7, 1, 4)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.lineEdit_contract_name = QtGui.QLineEdit(Form)
        self.lineEdit_contract_name.setObjectName(_fromUtf8("lineEdit_contract_name"))
        self.gridLayout.addWidget(self.lineEdit_contract_name, 0, 1, 1, 3)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)
        self.lineEdit_company_telephone = QtGui.QLineEdit(Form)
        self.lineEdit_company_telephone.setEnabled(False)
        self.lineEdit_company_telephone.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_company_telephone.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_company_telephone.setReadOnly(True)
        self.lineEdit_company_telephone.setObjectName(_fromUtf8("lineEdit_company_telephone"))
        self.gridLayout.addWidget(self.lineEdit_company_telephone, 1, 5, 1, 1)
        self.lineEdit_contract_number = QtGui.QLineEdit(Form)
        self.lineEdit_contract_number.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_contract_number.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_contract_number.setObjectName(_fromUtf8("lineEdit_contract_number"))
        self.gridLayout.addWidget(self.lineEdit_contract_number, 0, 5, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 10, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.doubleSpinBox_contract_amount = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBox_contract_amount.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_contract_amount.setMaximumSize(QtCore.QSize(150, 16777215))
        self.doubleSpinBox_contract_amount.setMaximum(999999999.99)
        self.doubleSpinBox_contract_amount.setObjectName(_fromUtf8("doubleSpinBox_contract_amount"))
        self.gridLayout.addWidget(self.doubleSpinBox_contract_amount, 0, 7, 1, 1)
        self.pushButton_preset_companies = QtGui.QPushButton(Form)
        self.pushButton_preset_companies.setObjectName(_fromUtf8("pushButton_preset_companies"))
        self.gridLayout.addWidget(self.pushButton_preset_companies, 1, 11, 1, 1)
        self.dateEdit_sign_date = QtGui.QDateEdit(Form)
        self.dateEdit_sign_date.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit_sign_date.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dateEdit_sign_date.setObjectName(_fromUtf8("dateEdit_sign_date"))
        self.gridLayout.addWidget(self.dateEdit_sign_date, 0, 11, 1, 1)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 8, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 9, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "合同名称", None))
        self.label_5.setText(_translate("Form", "合同供方", None))
        self.label_6.setText(_translate("Form", "联系人", None))
        self.label_2.setText(_translate("Form", "合同编号", None))
        self.lineEdit_contract_name.setText(_translate("Form", "测试用例合同名称随机", None))
        self.label_7.setText(_translate("Form", "联系电话", None))
        self.label_8.setText(_translate("Form", "联系地址", None))
        self.label_4.setText(_translate("Form", "签订日期", None))
        self.label_3.setText(_translate("Form", "合同金额", None))
        self.pushButton_preset_companies.setText(_translate("Form", "管理公司信息", None))
        self.dateEdit_sign_date.setDisplayFormat(_translate("Form", "yyyy-M-d", None))
        self.label_9.setText(_translate("Form", "合同类型", None))
