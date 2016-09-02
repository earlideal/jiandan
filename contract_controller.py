# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

import contract_template
import model
from model import session


class ContractWindow(QtGui.QWidget):
    def __init__(self):
        super(ContractWindow, self).__init__()
        self.ui = contract_template.Ui_Form()
        self.ui.setupUi(self)
        self._initialize_view()
        self.ui.pushButton.clicked.connect(self._update_model_from_view)

    def _initialize_view(self):
        self.ui.comboBox_company.currentIndexChanged.connect(self._update_company_info)
        companies = session.query(model.Company).all()
        self.company_names = []
        for company in companies:
            self.company_names.append(company.name)
        self.ui.comboBox_company.addItems(self.company_names)

        # 设置当天日期
        self.ui.dateEdit_sign_date.setDate(QtCore.QDate.currentDate())

    def _update_company_info(self):
        company_name = unicode(self.ui.comboBox_company.currentText())
        companies = session.query(model.Company).filter_by(name=company_name).all()
        c = companies[0]
        self.ui.lineEdit_company_contact.setText(c.contact)
        self.ui.lineEdit_company_telephone.setText(c.telephone)
        self.ui.lineEdit_company_address.setText(c.address)

    def _update_model_from_view(self):
        contract_name = unicode(self.ui.lineEdit_contract_name.text())
        contract_number = unicode(self.ui.lineEdit_contract_number.text())
        contract_amount = self.ui.doubleSpinBox_contract_amount.value()
        sign_date = self.ui.dateEdit_sign_date.date().toPyDate()
        company_name = unicode(self.ui.comboBox_company.currentText())
        companies = session.query(model.Company).filter_by(name=company_name).all()

        contract = model.Contract(contract_name=contract_name, contract_number=contract_number,
                                  contract_amount=contract_amount, sign_date=sign_date, company=companies[0])

        session.add(contract)
        session.commit()
        print u'合同信息存储成功'

    def _update_view_from_model(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    window = ContractWindow()
    window.show()
    app.exec_()
