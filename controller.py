# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import model
import requisition_template
from model import session


class RequisitionWindow(QtGui.QWidget):
    def __init__(self):
        super(RequisitionWindow, self).__init__()
        self.ui = requisition_template.Ui_Form()
        self.ui.setupUi(self)
        self._initialize()
        self.ui.toolButton_reason_gen.clicked.connect(self._update_model)

    def _initialize(self):
        # 添加采购方式
        self.ui.comboBox_purchase_method.addItems([u'', u'', u''])
        # 枚举数据库中的全部员工信息
        self.staffs = session.query(model.Staff).all()
        for s in self.staffs:
            self.ui.comboBox_applicant.addItem(s.name)
        self.ui.comboBox_applicant.setCurrentIndex(-1)
        # 枚举数据库中的全部基金信息
        self.projects = session.query(model.Project).all()
        for p in self.projects:
            self.ui.comboBox_project.addItem(p.grant_number)
        self.ui.comboBox_project.currentIndexChanged.connect(self.show_project_info)
        self.ui.comboBox_project.setCurrentIndex(-1)

    def show_project_info(self):
        text = unicode(self.ui.comboBox_project.currentText())
        if text == "":
            return
        p = session.query(model.Project).filter_by(grant_number=text).all()[0]
        info = p.leader.name + "-" + p.grant_type + "-" + p.name
        self.ui.lineEdit_project_info.setText(info)

    def _update_model(self):
        request_title = unicode(self.ui.lineEdit_request_title.text())
        request_applicant = unicode(self.ui.comboBox_applicant.currentText())
        request_date = unicode(self.ui.dateEdit_request_date.date())
        purchase_type = unicode(self.ui.comboBox_purchase_type.currentText())
        grant_number = unicode(self.ui.comboBox_project.currentText())
        purchase_method = unicode(self.ui.comboBox_purchase_method.currentText())
        is_budget = self.ui.radioButton_yes.isChecked()
        if is_budget:
            budget_value = self.ui.doubleSpinBox_budget.value()
            budget = self.ui.doubleSpinBox_budget.text()
        else:
            budget = ''
        purchase_reason = unicode(self.ui.lineEdit_purchase_reason.text())
        tech_specification = unicode(self.ui.lineEdit_tech_spec.text())
        # TODO
        # 需要检查表单为空的情况
        staffs = session.query(model.Staff).filter_by(name=request_applicant).all()
        if len(staffs) == 0:
            raise u'严重错误！未在数据库中找到选择的申请人，请联系系统管理员。'

        projects = session.query(model.Project).filter_by(grant_number=grant_number).all()
        if len(projects) == 0:
            raise u'严重错误！未在数据库中找到选择的课题号，请联系系统管理员。'

        requisition = Requisition(title=request_title, applicant=staffs[0], project=projects[0],
                                  purchase_method=u'公开招标',
                                  purchase_reason=u'该项目是中科院修购专项批准购买的专项设备。')
        session.add(requisition)
        session.commit()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('lucida console', 9))
    window = RequisitionWindow()
    window.show()
    app.setStyle('windowsxp')
    app.exec_()
