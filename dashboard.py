from PyQt4 import QtGui

import dashboard_template
from acceptance_controller import AcceptanceWindow
from contract_controller import ContractWindow
from inventory_controller import InventoryWindow
from printer_controller import PrinterWindow
from requisition_controller import RequisitionWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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
    app.setStyle('plastique')
    window = MainWindow()
    window.showMaximized()
    app.exec_()
