from PyQt4 import QtGui

from acceptance import AcceptanceWindow
from contract import ContractWindow
from inventory import InventoryWindow
from printer import PrinterWindow
from requisition import RequisitionWindow
from views import dashboard_template


class TransactionWindow(QtGui.QWidget):
    def __init__(self):
        super(TransactionWindow, self).__init__()
        self.ui = dashboard_template.Ui_MainWindow()
        self.ui.setupUi(self)

        self.reqisition_window = RequisitionWindow()
        self.contract_window = ContractWindow()
        self.acceptance_window = AcceptanceWindow()
        self.printer_window = PrinterWindow()
        self.inventory_window = InventoryWindow()

        self.ui.verticalLayout_requisition_tab.addWidget(self.reqisition_window)
        self.ui.verticalLayout_contract_tab.addWidget(self.contract_window)
        self.ui.verticalLayout_acceptance_tab.addWidget(self.acceptance_window)
        self.ui.horizontalLayout_inventory.addWidget(self.inventory_window)
        self.ui.verticalLayout_printer_tab.addWidget(self.printer_window)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('book antiqua', 9))
    app.setStyle('windows')
    window = TransactionWindow()
    window.showMaximized()
    app.exec_()
