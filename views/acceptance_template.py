# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acceptance_template.ui'
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
        Form.resize(864, 104)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1)
        self.dateEdit_acceptance_date = QtGui.QDateEdit(Form)
        self.dateEdit_acceptance_date.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit_acceptance_date.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dateEdit_acceptance_date.setObjectName(_fromUtf8("dateEdit_acceptance_date"))
        self.gridLayout.addWidget(self.dateEdit_acceptance_date, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 6, 1, 1)
        self.comboBox_transactor = QtGui.QComboBox(Form)
        self.comboBox_transactor.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_transactor.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_transactor.setObjectName(_fromUtf8("comboBox_transactor"))
        self.gridLayout.addWidget(self.comboBox_transactor, 0, 1, 1, 1)
        self.lineEdit_acceptance_place = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_acceptance_place.sizePolicy().hasHeightForWidth())
        self.lineEdit_acceptance_place.setSizePolicy(sizePolicy)
        self.lineEdit_acceptance_place.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_acceptance_place.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_acceptance_place.setObjectName(_fromUtf8("lineEdit_acceptance_place"))
        self.gridLayout.addWidget(self.lineEdit_acceptance_place, 0, 5, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.frame_standard = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_standard.sizePolicy().hasHeightForWidth())
        self.frame_standard.setSizePolicy(sizePolicy)
        self.frame_standard.setFrameShape(QtGui.QFrame.Box)
        self.frame_standard.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_standard.setObjectName(_fromUtf8("frame_standard"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_standard)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_14 = QtGui.QCheckBox(self.frame_standard)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.horizontalLayout_2.addWidget(self.checkBox_14)
        self.checkBox_13 = QtGui.QCheckBox(self.frame_standard)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.horizontalLayout_2.addWidget(self.checkBox_13)
        self.checkBox_12 = QtGui.QCheckBox(self.frame_standard)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.horizontalLayout_2.addWidget(self.checkBox_12)
        self.checkBox_11 = QtGui.QCheckBox(self.frame_standard)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.horizontalLayout_2.addWidget(self.checkBox_11)
        self.gridLayout.addWidget(self.frame_standard, 0, 7, 1, 1)
        self.comboBox_feature_test = QtGui.QComboBox(Form)
        self.comboBox_feature_test.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_feature_test.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_feature_test.setObjectName(_fromUtf8("comboBox_feature_test"))
        self.gridLayout.addWidget(self.comboBox_feature_test, 2, 1, 1, 1)
        self.comboBox_quality_test = QtGui.QComboBox(Form)
        self.comboBox_quality_test.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_quality_test.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_quality_test.setObjectName(_fromUtf8("comboBox_quality_test"))
        self.gridLayout.addWidget(self.comboBox_quality_test, 2, 3, 1, 1)
        self.frame_documents = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_documents.sizePolicy().hasHeightForWidth())
        self.frame_documents.setSizePolicy(sizePolicy)
        self.frame_documents.setFrameShape(QtGui.QFrame.Box)
        self.frame_documents.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_documents.setObjectName(_fromUtf8("frame_documents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_documents)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_7 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.horizontalLayout.addWidget(self.checkBox_7)
        self.checkBox_1 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.checkBox_9 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.horizontalLayout.addWidget(self.checkBox_9)
        self.checkBox_8 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.horizontalLayout.addWidget(self.checkBox_8)
        self.checkBox_6 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.checkBox = QtGui.QCheckBox(self.frame_documents)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_5 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.checkBox_4 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtGui.QCheckBox(self.frame_documents)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.gridLayout.addWidget(self.frame_documents, 1, 1, 1, 7)
        self.comboBox_specification_test = QtGui.QComboBox(Form)
        self.comboBox_specification_test.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_specification_test.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_specification_test.setObjectName(_fromUtf8("comboBox_specification_test"))
        self.gridLayout.addWidget(self.comboBox_specification_test, 2, 5, 1, 1)
        self.lineEdit_test_report = QtGui.QLineEdit(Form)
        self.lineEdit_test_report.setObjectName(_fromUtf8("lineEdit_test_report"))
        self.gridLayout.addWidget(self.lineEdit_test_report, 2, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_7.setText(_translate("Form", "质量测试", None))
        self.label_6.setText(_translate("Form", "外观测试", None))
        self.label_8.setText(_translate("Form", "指标测试", None))
        self.label_9.setText(_translate("Form", "测试报告", None))
        self.label.setText(_translate("Form", "验收时间", None))
        self.label_3.setText(_translate("Form", "验收地点", None))
        self.label_2.setText(_translate("Form", "验收经办", None))
        self.label_4.setText(_translate("Form", "验收依据", None))
        self.label_5.setText(_translate("Form", "资料附件", None))
        self.checkBox_14.setText(_translate("Form", "标准", None))
        self.checkBox_13.setText(_translate("Form", "招标文件", None))
        self.checkBox_12.setText(_translate("Form", "合同", None))
        self.checkBox_11.setText(_translate("Form", "图纸", None))
        self.checkBox_7.setText(_translate("Form", "决算单", None))
        self.checkBox_1.setText(_translate("Form", "操作手册", None))
        self.checkBox_9.setText(_translate("Form", "研究报告", None))
        self.checkBox_8.setText(_translate("Form", "测试报告", None))
        self.checkBox_6.setText(_translate("Form", "质保书", None))
        self.checkBox.setText(_translate("Form", "合格证", None))
        self.checkBox_5.setText(_translate("Form", "装箱清单", None))
        self.checkBox_4.setText(_translate("Form", "商检证书", None))
        self.checkBox_3.setText(_translate("Form", "保修手册", None))
        self.checkBox_2.setText(_translate("Form", "安装手册", None))
