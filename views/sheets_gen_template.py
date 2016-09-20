# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sheets_gen_template.ui'
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
        Dialog.resize(494, 290)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_basic = QtGui.QGroupBox(Dialog)
        self.groupBox_basic.setFlat(True)
        self.groupBox_basic.setCheckable(True)
        self.groupBox_basic.setObjectName(_fromUtf8("groupBox_basic"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_basic)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_basic)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.checkBox_verification_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_verification_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_verification_sheet.setObjectName(_fromUtf8("checkBox_verification_sheet"))
        self.gridLayout.addWidget(self.checkBox_verification_sheet, 4, 1, 1, 1)
        self.checkBox_facility_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_facility_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_facility_sheet.setObjectName(_fromUtf8("checkBox_facility_sheet"))
        self.gridLayout.addWidget(self.checkBox_facility_sheet, 4, 3, 1, 1)
        self.checkBox_requisition_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_requisition_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_requisition_sheet.setObjectName(_fromUtf8("checkBox_requisition_sheet"))
        self.gridLayout.addWidget(self.checkBox_requisition_sheet, 4, 0, 1, 1)
        self.checkBox_lading_bill_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_lading_bill_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_lading_bill_sheet.setObjectName(_fromUtf8("checkBox_lading_bill_sheet"))
        self.gridLayout.addWidget(self.checkBox_lading_bill_sheet, 4, 2, 1, 1)
        self.lineEdit_title = QtGui.QLineEdit(self.groupBox_basic)
        self.lineEdit_title.setEnabled(False)
        self.lineEdit_title.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.gridLayout.addWidget(self.lineEdit_title, 1, 1, 1, 3)
        self.checkBox_title_with_list = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_title_with_list.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_title_with_list.setObjectName(_fromUtf8("checkBox_title_with_list"))
        self.gridLayout.addWidget(self.checkBox_title_with_list, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_basic)
        self.groupBox_extra = QtGui.QGroupBox(Dialog)
        self.groupBox_extra.setFlat(True)
        self.groupBox_extra.setCheckable(True)
        self.groupBox_extra.setChecked(False)
        self.groupBox_extra.setObjectName(_fromUtf8("groupBox_extra"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_extra)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_verification_review_table = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_verification_review_table.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_verification_review_table.setObjectName(_fromUtf8("checkBox_verification_review_table"))
        self.gridLayout_2.addWidget(self.checkBox_verification_review_table, 3, 2, 1, 1)
        self.checkBox_contract_review_table = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_contract_review_table.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_contract_review_table.setObjectName(_fromUtf8("checkBox_contract_review_table"))
        self.gridLayout_2.addWidget(self.checkBox_contract_review_table, 3, 1, 1, 1)
        self.checkBox_requisition_review_table = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_requisition_review_table.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_requisition_review_table.setObjectName(_fromUtf8("checkBox_requisition_review_table"))
        self.gridLayout_2.addWidget(self.checkBox_requisition_review_table, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_extra)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.checkBox_multiple_equipments = QtGui.QCheckBox(self.groupBox_extra)
        self.checkBox_multiple_equipments.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_multiple_equipments.setObjectName(_fromUtf8("checkBox_multiple_equipments"))
        self.gridLayout_2.addWidget(self.checkBox_multiple_equipments, 0, 0, 1, 2)
        self.lineEdit_equipment_name = QtGui.QLineEdit(self.groupBox_extra)
        self.lineEdit_equipment_name.setEnabled(False)
        self.lineEdit_equipment_name.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_equipment_name.setObjectName(_fromUtf8("lineEdit_equipment_name"))
        self.gridLayout_2.addWidget(self.lineEdit_equipment_name, 1, 1, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_extra)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_generate = QtGui.QPushButton(Dialog)
        self.pushButton_generate.setObjectName(_fromUtf8("pushButton_generate"))
        self.horizontalLayout.addWidget(self.pushButton_generate)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_generate, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_basic.setTitle(_translate("Dialog", "采购基本单据", None))
        self.label.setText(_translate("Dialog", "统一抬头：", None))
        self.checkBox_verification_sheet.setText(_translate("Dialog", "检验单", None))
        self.checkBox_facility_sheet.setText(_translate("Dialog", "设备卡", None))
        self.checkBox_requisition_sheet.setText(_translate("Dialog", "请购单", None))
        self.checkBox_lading_bill_sheet.setText(_translate("Dialog", "直发单", None))
        self.checkBox_title_with_list.setText(_translate("Dialog", "采用标题加明细的方式生成单据", None))
        self.groupBox_extra.setTitle(_translate("Dialog", "采购附加单据 【总金额大于5万元】", None))
        self.checkBox_verification_review_table.setText(_translate("Dialog", "仪器设备验收单", None))
        self.checkBox_contract_review_table.setText(_translate("Dialog", "采购合同评审表", None))
        self.checkBox_requisition_review_table.setText(_translate("Dialog", "采购申请评审表", None))
        self.label_2.setText(_translate("Dialog", "统一名称：", None))
        self.checkBox_multiple_equipments.setText(_translate("Dialog", "设备名称非单一", None))
        self.pushButton_generate.setText(_translate("Dialog", "生成", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))
