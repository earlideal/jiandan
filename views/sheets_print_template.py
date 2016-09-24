# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sheets_print_template.ui'
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
        Dialog.resize(750, 262)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_gen = QtGui.QVBoxLayout()
        self.verticalLayout_gen.setObjectName(_fromUtf8("verticalLayout_gen"))
        self.groupBox_basic = QtGui.QGroupBox(Dialog)
        self.groupBox_basic.setCheckable(True)
        self.groupBox_basic.setObjectName(_fromUtf8("groupBox_basic"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_basic)
        self.gridLayout.setContentsMargins(25, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_basic)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.checkBox_requisition_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_requisition_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_requisition_sheet.setObjectName(_fromUtf8("checkBox_requisition_sheet"))
        self.gridLayout.addWidget(self.checkBox_requisition_sheet, 4, 0, 1, 1)
        self.checkBox_verification_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_verification_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_verification_sheet.setObjectName(_fromUtf8("checkBox_verification_sheet"))
        self.gridLayout.addWidget(self.checkBox_verification_sheet, 4, 1, 1, 1)
        self.checkBox_facility_sheet = QtGui.QCheckBox(self.groupBox_basic)
        self.checkBox_facility_sheet.setMinimumSize(QtCore.QSize(110, 0))
        self.checkBox_facility_sheet.setObjectName(_fromUtf8("checkBox_facility_sheet"))
        self.gridLayout.addWidget(self.checkBox_facility_sheet, 4, 3, 1, 1)
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
        self.verticalLayout_gen.addWidget(self.groupBox_basic)
        self.groupBox_extra = QtGui.QGroupBox(Dialog)
        self.groupBox_extra.setCheckable(True)
        self.groupBox_extra.setChecked(False)
        self.groupBox_extra.setObjectName(_fromUtf8("groupBox_extra"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_extra)
        self.gridLayout_2.setContentsMargins(25, -1, -1, -1)
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
        self.verticalLayout_gen.addWidget(self.groupBox_extra)
        self.horizontalLayout_2.addLayout(self.verticalLayout_gen)
        self.verticalLayout_tools = QtGui.QVBoxLayout()
        self.verticalLayout_tools.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_tools.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_tools.setObjectName(_fromUtf8("verticalLayout_tools"))
        self.toolButton_generate = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_generate.sizePolicy().hasHeightForWidth())
        self.toolButton_generate.setSizePolicy(sizePolicy)
        self.toolButton_generate.setAutoRaise(True)
        self.toolButton_generate.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_generate.setObjectName(_fromUtf8("toolButton_generate"))
        self.verticalLayout_tools.addWidget(self.toolButton_generate)
        self.horizontalLayout_2.addLayout(self.verticalLayout_tools)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_frame = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_frame.setObjectName(_fromUtf8("verticalLayout_frame"))
        self.verticalLayout_sheets = QtGui.QVBoxLayout()
        self.verticalLayout_sheets.setSpacing(0)
        self.verticalLayout_sheets.setObjectName(_fromUtf8("verticalLayout_sheets"))
        self.verticalLayout_frame.addLayout(self.verticalLayout_sheets)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.checkBox_title_with_list, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               self.lineEdit_title.setEnabled)
        QtCore.QObject.connect(self.checkBox_multiple_equipments, QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                               self.lineEdit_equipment_name.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.groupBox_basic.setTitle(_translate("Dialog", "采购基本单据", None))
        self.label.setText(_translate("Dialog", "统一抬头：", None))
        self.checkBox_requisition_sheet.setText(_translate("Dialog", "请购单", None))
        self.checkBox_verification_sheet.setText(_translate("Dialog", "检验单", None))
        self.checkBox_facility_sheet.setText(_translate("Dialog", "设备卡", None))
        self.checkBox_lading_bill_sheet.setText(_translate("Dialog", "直发单", None))
        self.checkBox_title_with_list.setText(_translate("Dialog", "采用明细清单方式", None))
        self.groupBox_extra.setTitle(_translate("Dialog", "采购附加单据 【总金额大于5万元】", None))
        self.checkBox_verification_review_table.setText(_translate("Dialog", "仪器设备验收单", None))
        self.checkBox_contract_review_table.setText(_translate("Dialog", "采购合同评审表", None))
        self.checkBox_requisition_review_table.setText(_translate("Dialog", "采购申请评审表", None))
        self.label_2.setText(_translate("Dialog", "统一名称：", None))
        self.checkBox_multiple_equipments.setText(_translate("Dialog", "采用统一设备名称方式", None))
        self.toolButton_generate.setText(_translate("Dialog", "...", None))
