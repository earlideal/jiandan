# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

import model
from model import session
from views import contract_template


class ContractWidget(QtGui.QWidget):
    def __init__(self):
        super(ContractWidget, self).__init__()
        self.ui = contract_template.Ui_Form()
        self.ui.setupUi(self)
        self._initialize_view()
        self.ui.pushButton_preset_companies.clicked.connect(self._update_view_from_model)

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
        contract_name = u'代理进口协议示例一'
        contract = session.query(model.Contract).filter_by(contract_name=contract_name).first()
        if contract is not None:
            self.ui.lineEdit_contract_name.setText(contract.contract_name)
            self.ui.lineEdit_contract_number.setText(contract.contract_number)
            self.ui.doubleSpinBox_contract_amount.setValue(contract.contract_amount)
            self.ui.dateEdit_sign_date.setDate(contract.sign_date)
            name = contract.company.name
            self.ui.comboBox_company.setCurrentIndex(self.company_names.index(name))
            self._update_company_info()
