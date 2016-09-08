from PyQt4 import QtGui

from acceptance import AcceptanceWidget
from contract import ContractWidget
from inventory import InventoryWidget
from printer import PrinterWidget
from requisition import RequisitionWidget
from views import transaction_template


class TransactionWidget(QtGui.QWidget):
    def __init__(self):
        super(TransactionWidget, self).__init__()
        self.ui = transaction_template.Ui_Form()
        self.ui.setupUi(self)

        self.reqisition_widget = RequisitionWidget()
        self.contract_widget = ContractWidget()
        self.acceptance_widget = AcceptanceWidget()
        self.printer_widget = PrinterWidget()
        self.inventory_widget = InventoryWidget()

        self.ui.verticalLayout_requisition_tab.addWidget(self.reqisition_widget)
        self.ui.verticalLayout_contract_tab.addWidget(self.contract_widget)
        self.ui.verticalLayout_acceptance_tab.addWidget(self.acceptance_widget)
        self.ui.horizontalLayout_inventory.addWidget(self.inventory_widget)
        self.ui.verticalLayout_printer_tab.addWidget(self.printer_widget)
