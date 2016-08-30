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
        names = [u'苏付海', u'刘晓迪', u'杨雪', u'姜树清', u'丁俊峰', u'王媛', u'蒋华超']
        names.sort()
        for n in names:
            print n
        staffs = session.query(model.Staff).all()
        for s in staffs:
            self.ui.comboBox_applicant.addItem(s.name)

    def _update_model(self):
        request_title = unicode(self.ui.lineEdit_request_title.text())
        request_applicant = unicode(self.ui.comboBox_applicant.currentText())
        request_date = unicode(self.ui.dateEdit_request_date.date())
        purchase_type = unicode(self.ui.comboBox_purchase_type.currentText())
        grant_number = unicode(self.ui.comboBox_project.currentText())
        purchase_method = unicode(self.ui.comboBox_purchase_method.currentText())
        is_budget = self.ui.radioButton_yes.isChecked()  # True/False
        if is_budget:
            budget_value = self.ui.doubleSpinBox_budget.value()
            budget = self.ui.doubleSpinBox_budget.text()
        else:
            budget = ''
        purchase_reason = unicode(self.ui.lineEdit_purchase_reason.text())
        tech_specification = unicode(self.ui.lineEdit_tech_spec.text())

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
    app.setFont(QtGui.QFont('Trebuchet MS', 9))
    window = RequisitionWindow()
    window.show()
    app.setStyle('windowsxp')
    app.exec_()
