# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

import model
from model import session
from view_templates import requisition_template


class RequisitionWindow(QtGui.QWidget):
    def __init__(self):
        super(RequisitionWindow, self).__init__()
        self.ui = requisition_template.Ui_Form()
        self.ui.setupUi(self)
        self._initialize_view()
        self.ui.pushButton_preset_reasons.clicked.connect(self._update_view_from_model)

    def _initialize_view(self):
        # TODO 将标签内容全部右对齐
        for label in self.ui.gridLayout.findChildren(QtGui.QLabel):
            print label.objectName()

        # 读取数据库中采购分类表，并显示在界面上
        categories = session.query(model.PurchaseCategory).all()
        self.category_names = []
        for category in categories:
            self.ui.comboBox_purchase_category.addItem(category.name)
            self.category_names.append(category.name)

        # 读取数据库中采购方式表，并显示在界面上
        methods = session.query(model.PurchaseMethod).all()
        self.method_names = []
        for m in methods:
            self.ui.comboBox_purchase_method.addItem(m.name)
            self.method_names.append(m.name)

        # 枚举数据库中的全部员工信息
        staffs = session.query(model.Staff).all()
        self.staff_names = []
        for s in staffs:
            self.staff_names.append(s.name)

        # 将员工按照顺序排列显示，其中排列方式是unicode码，不是拼音
        self.staff_names.sort()
        self.ui.comboBox_applicant.addItems(self.staff_names)
        self.ui.comboBox_applicant.setCurrentIndex(0)
        # 枚举数据库中的全部基金信息
        self.ui.comboBox_project.currentIndexChanged.connect(self._update_project_info)
        projects = session.query(model.Project).all()
        self.grant_numbers = []
        for p in projects:
            self.ui.comboBox_project.addItem(p.grant_number)
            self.grant_numbers.append(p.grant_number)

        # 设置当天日期
        self.ui.dateEdit_request_date.setDate(QtCore.QDate.currentDate())

    def _update_project_info(self):
        # 根据选择的课题号显示出课题基本信息
        text = unicode(self.ui.comboBox_project.currentText())
        if text == "":
            return
        p = session.query(model.Project).filter_by(grant_number=text).first()
        info = p.leader.name + "-" + p.grant_type + "-" + p.name
        self.ui.lineEdit_project_info.setText(info)

    def _update_model_from_view(self):
        request_title = unicode(self.ui.lineEdit_request_title.text())
        request_applicant = unicode(self.ui.comboBox_applicant.currentText())
        request_date = self.ui.dateEdit_request_date.date().toPyDate()
        grant_number = unicode(self.ui.comboBox_project.currentText())
        purchase_category = unicode(self.ui.comboBox_purchase_category.currentText())
        purchase_method = unicode(self.ui.comboBox_purchase_method.currentText())
        is_budget = self.ui.radioButton_yes.isChecked()
        if is_budget:
            budget_value = self.ui.doubleSpinBox_budget.value()
        else:
            budget_value = 0
        request_reason = unicode(self.ui.lineEdit_request_reason.text())
        technical_spec = unicode(self.ui.lineEdit_tech_spec.text())

        # TODO 需要检查表单为空的情况

        staff = session.query(model.Staff).filter_by(name=request_applicant).first()
        proj = session.query(model.Project).filter_by(grant_number=grant_number).first()
        category = session.query(model.PurchaseCategory).filter_by(name=purchase_category).first()
        methods = session.query(model.PurchaseMethod).filter_by(name=purchase_method).first()

        # TODO 此处需要对添加和修改做判断，并作不同处理

        requisition = model.Requisition(title=request_title, applicant=staff, project=proj,
                                        purchase_category=category, is_budget=is_budget,
                                        budget_amount=budget_value, purchase_method=methods,
                                        request_reason=u'该项目是中科院修购专项批准购买的专项设备。')
        session.add(requisition)
        session.commit()
        print u'添加请购信息成功！'

    def _update_view_from_model(self):
        title = u'大功率飞秒激光器系统'
        req = session.query(model.Requisition).filter_by(title=title).first()
        if req is not None:
            self.ui.lineEdit_request_title.setText(r.title)
            self.ui.comboBox_applicant.setCurrentIndex(self.staff_names.index(r.applicant.name))
            self.ui.dateEdit_request_date.setDate(r.date)
            self.ui.comboBox_project.setCurrentIndex(self.grant_numbers.index(r.project.grant_number))
            self.ui.comboBox_purchase_category.setCurrentIndex(self.category_names.index(r.purchase_category.name))
            self.ui.comboBox_purchase_method.setCurrentIndex(self.method_names.index(r.purchase_method.name))
            self.ui.radioButton_yes.setChecked(r.is_budget)
            self.ui.lineEdit_request_reason.setText(r.request_reason)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    window = RequisitionWindow()
    window.show()
    app.exec_()
