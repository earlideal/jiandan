# -*- coding: utf-8 -*-
import os
from functools import partial

from PyQt4 import QtGui
from win32com.client import Dispatch

import model
from views import sheets_print_template


class PrintDialog(QtGui.QDialog):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.ui = sheets_print_template.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toolButton_generate.clicked.connect(self._generate_sheets_file)

        self.sheets_name_en = ['REQUISITION_SHEET', 'REQUISITION_REVIEW_TABLE', 'CONTRACT_REVIEW_TABLE',
                               'VERIFICATION_SHEET', 'VERIFICATION_REVIEW_TABLE', 'LADING_BILL_SHEET', 'FACILITY_SHEET']
        self.sheets_name_zh = {'REQUISITION_SHEET': u'请购单',
                               'REQUISITION_REVIEW_TABLE': u'采购申请评审表',
                               'CONTRACT_REVIEW_TABLE': u'采购合同评审表',
                               'VERIFICATION_SHEET': u'检验单',
                               'VERIFICATION_REVIEW_TABLE': u'仪器设备验收单',
                               'LADING_BILL_SHEET': u'直发单',
                               'FACILITY_SHEET': u'设备卡'}

    def _generate_sheets_file(self):
        # temp = (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(8)))).upper()
        temp = 'temp'
        path = os.path.abspath(temp)
        if not os.path.exists(path):
            os.mkdir(temp)
        to_be_generated = {'REQUISITION_SHEET': True,
                           'REQUISITION_REVIEW_TABLE': False,
                           'CONTRACT_REVIEW_TABLE': False,
                           'VERIFICATION_SHEET': False,
                           'VERIFICATION_REVIEW_TABLE': False,
                           'LADING_BILL_SHEET': False,
                           'FACILITY_SHEET': False}

        # 遍历对话框中的checkbox组件，通过其objectName与sheets名称进行对应
        for child in self.children():
            if isinstance(child, QtGui.QGroupBox):
                for c in child.children():
                    if isinstance(c, QtGui.QCheckBox):
                        name = c.objectName()
                        name = unicode(name[9:]).upper()
                        if to_be_generated.has_key(name):
                            if c.isChecked() and c.isEnabled():
                                to_be_generated[name] = True
                            else:
                                to_be_generated[name] = False

        self._fill_sheets_blanks(to_be_generated)

    def _fill_sheets_blanks(self, to_be_generated):
        word = get_microsoft_word()
        dir = os.getcwd() + os.path.sep + 'sheets' + os.path.sep
        transaction = model.session.query(model.Transaction).first()
        requisition = transaction.requisition
        req_title = requisition.title
        req_date = requisition.date
        req_applicant = requisition.applicant
        req_purchase_method = requisition.purchase_method
        req_purchase_category = requisition.purchase_category
        req_project = requisition.project
        req_is_budget = requisition.is_budget
        req_budget_amount = requisition.budget_amount
        req_reason = requisition.request_reason
        req_tech_spec = requisition.technical_spec

        contract = transaction.contract
        cont_name = contract.name
        cont_number = contract.number
        cont_amount = contract.amount
        cont_sign_date = contract.sign_date
        cont_company = contract.company

        items = model.session.query(model.Inventory).filter_by(swift_code=transaction.swift_code).all()
        items_count = len(items)

        #####################################
        # 请购单
        #####################################
        file = u'REQUISITION_SHEET.docx'
        sheet_name = file.split('.')[0]
        if to_be_generated[sheet_name]:
            print u'正在生成%s ...' % self.sheets_name_zh[sheet_name]
            path = dir + file
            ROW_COUNT = 8

            paper_pieces = items_count / ROW_COUNT
            remaining = items_count % ROW_COUNT
            if remaining > 0:
                paper_pieces = paper_pieces + 1

            for i in xrange(0, paper_pieces):
                document = word.Documents.Open(path)
                fill_cell_with_text(document, [1, 1, 4], req_project.grant_number)
                fill_cell_with_text(document, [1, 1, 8], req_date)

                for j in xrange(0, ROW_COUNT):
                    m = i * ROW_COUNT + j
                    if m >= items_count:
                        break
                    item = items[m]
                    name = item.name
                    model_type = item.model
                    unit = item.unit
                    quantity = item.quantity
                    price = item.requisition_price
                    dummy = ''
                    sum = item.requisition_sum
                    data = [name, model_type, unit, quantity, price, dummy, sum]
                    for c in xrange(0, 7):
                        fill_cell_with_text(document, [2, j + 1, c + 1], data[c])

                file = u'REQUISITION_SHEET_%s.docx' % (i + 1)
                word.ActiveDocument.SaveAs(file)
                word.ActiveDocument.Close()
            self._generate_print_list(sheet_name, paper_pieces)

        #####################################
        # 采购申请评审表
        #####################################
        file = u'REQUISITION_REVIEW_TABLE.docx'
        sheet_name = file.split('.')[0]
        if to_be_generated[sheet_name]:
            print u'正在生成%s ...' % self.sheets_name_zh[sheet_name]
            path = dir + file
            document = word.Documents.Open(path)
            reason_tech_spec = u'采购理由：' + req_reason + '\n' + u'技术指标：'  # + req_tech_spec
            data = [req_title, req_purchase_category.name, [u'否', u'是'][req_is_budget], req_budget_amount,
                    req_project.grant_number, req_purchase_method.name, reason_tech_spec]
            cells = [[1, 1, 2], [1, 2, 2], [1, 3, 2], [1, 3, 4], [1, 3, 6], [1, 4, 2], [1, 5, 2]]
            for c in xrange(len(cells)):
                fill_cell_with_text(document, cells[c], data[c])
            file = u'REQUISITION_REVIEW_TABLE_1.docx'
            word.ActiveDocument.SaveAs(file)
            word.ActiveDocument.Close()
            self._generate_print_list(sheet_name, 1)

        #####################################
        # 合同评审表
        #####################################

        #####################################
        # 检验单
        #####################################
        file = u'VERIFICATION_SHEET.docx'
        sheet_name = file.split('.')[0]
        if to_be_generated[sheet_name]:
            print u'正在生成%s ...' % self.sheets_name_zh[sheet_name]
            path = dir + file

            ROW_COUNT = 1
            paper_pieces = items_count / ROW_COUNT

            for i in xrange(0, paper_pieces):
                document = word.Documents.Open(path)
                grant_num = req_project.grant_number
                for j in xrange(0, ROW_COUNT):
                    m = i * ROW_COUNT + j
                    if m >= items_count:
                        break
                    item = items[m]
                    name = item.name
                    model_type = item.model
                    unit = item.unit
                    quantity = item.quantity
                    manufacture = u'京东商城'
                    price = item.requisition_price
                    sum = item.requisition_sum
                    data = [[name, model_type],
                            [quantity, quantity],
                            [manufacture, price],
                            [grant_num, '']]
                    for r in xrange(0, 4):
                        for c in xrange(0, 2):
                            fill_cell_with_text(document, [1, r + 1, (c + 1) * 2], data[r][c])

                file = u'VERIFICATION_SHEET_%s.docx' % (i + 1)
                word.ActiveDocument.SaveAs(file)
                word.ActiveDocument.Close()
                self._generate_print_list(sheet_name, paper_pieces)

        #####################################
        # 设备验收表
        #####################################

        #####################################
        # 直发单
        #####################################

        #####################################
        # 设备卡
        #####################################
        print u'数据表生成完成！'
        word.Quit()

    def _generate_print_list(self, sheet_name_en, total_sheets_num):

        # 生成打印项目前，需要先清除之前生成的项目
        # frame.children()仅仅列出来最基础一层布局，不会列出来子布局
        # 想要列出子布局，必须用子布局的父级进行枚举，但这种方式不能枚举出子widget
        for child in self.ui.frame.children():
            if isinstance(child, QtGui.QWidget):
                self.ui.verticalLayout_sheets.removeWidget(child)
                child.deleteLater()
        for child in self.ui.verticalLayout_sheets.children():
            self.ui.verticalLayout_sheets.removeItem(child)

        label_req = QtGui.QLabel()
        label_req.setText(self.sheets_name_zh[sheet_name_en])
        sheet_buttons = []
        font = QtGui.QFont()
        font.setUnderline(True)
        for i in xrange(1, total_sheets_num + 1):
            toolButton = QtGui.QToolButton()
            toolButton.setFont(font)
            toolButton.setAutoRaise(True)
            toolButton.setObjectName(sheet_name_en)
            toolButton.setText(str(i))
            name = sheet_name_en + '_' + str(i) + '.docx'
            sheet_buttons.append(toolButton)
            # 此处不能使用lambda表达式，会总是打开最后一个赋值的文件
            toolButton.clicked.connect(partial(self.print_relevant_sheet, name))
        hbox = QtGui.QHBoxLayout()
        hbox.setSpacing(0)
        hbox.addWidget(label_req)
        for x in sheet_buttons:
            hbox.addWidget(x)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        hbox.addItem(spacerItem)
        self.ui.verticalLayout_sheets.addLayout(hbox)

    def print_relevant_sheet(self, file_name):
        # 此处困扰了我很久
        # 在该方法中，word打开的文档路径不能与点击的按钮本身有任何联系（如按钮的text()作为文件名等）
        # 否则会导致堆栈溢出错误，原因不明
        # 传递一般文本作为路径是可行的
        path = 'C:\Users\John\Documents' + os.path.sep + file_name
        print path
        word = get_microsoft_word()
        document = word.Documents.Open(path)
        document.PrintOut()
        document.Close()


def fill_cell_with_text(document, position, text):
    if len(position) == 3:
        table_seq = position[0]
        row_seq = position[1]
        col_seq = position[2]
        cell = document.Tables(table_seq).Cell(Row=row_seq, Column=col_seq)
        cell.Range.Text = text


def get_microsoft_word():
    # 通过pywin32调用word程序
    application = Dispatch('Word.Application')
    application.Visible = 0
    application.DisplayAlerts = 0
    return application


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setFont(QtGui.QFont('trebuchet ms', 9))
    app.setStyle('windowsvista')
    dialog = PrintDialog()
    dialog.show()
    app.exec_()
