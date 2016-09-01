# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import contract_template
import model
from model import session


class ContractWindow(QtGui.QWidget):
    def __init__(self):
        super(ContractWindow, self).__init__()
        self.ui = contract_template.Ui_Form()
        self.ui.setupUi(self)
        self._initialize_view()
        self.ui.pushButton.clicked.connect()

    def _initialize_view(self):
        companies = session.query(model.Company).all()
        company_names = []
        for company in companies:
            company_names.append(company.name)
        self.ui.comboBox_company.additems(company_names)
