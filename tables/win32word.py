# -*- coding: utf-8 -*-

from win32com.client import Dispatch

import model


class WordSheetsHandler(object):
    def __init__(self):
        super(WordSheetsHandler, self).__init__()
        self.word_application = Dispatch('Word.Application')
        self.word_application.Visible = 1
        self.word_application.DisplayAlerts = 0

        # self._fill_blanks()
        self._quit_word_application()

    def _fill_blanks(self):
        disassemble_word_tables(self.word_application)

    def _quit_word_application(self):
        self.word_application.Quit()


def disassemble_word_tables(application):
    dir = 'C:\\Users\\John\\Documents\\PYTHON\\jiandan\\templates\\'

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
    path = dir + file

    ROW_COUNT = 8
    paper_pieces = items_count / ROW_COUNT
    remaining = items_count % ROW_COUNT
    if remaining > 0:
        paper_pieces = paper_pieces + 1

    for i in xrange(0, paper_pieces):
        document = application.Documents.Open(path)
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
        application.ActiveDocument.SaveAs(file)
        application.ActiveDocument.Close()

    #####################################
    # 采购申请评审表
    #####################################
    file = u'REQUISITION_REVIEW_TABLE.docx'
    path = dir + file
    document = application.Documents.Open(path)
    reason_tech_spec = u'采购理由：' + req_reason + '\n' + u'技术指标：'  # + req_tech_spec
    data = [req_title, req_purchase_category.name, [u'否', u'是'][req_is_budget], req_budget_amount,
            req_project.grant_number, req_purchase_method.name, reason_tech_spec]
    cells = [[1, 1, 2], [1, 2, 2], [1, 3, 2], [1, 3, 4], [1, 3, 6], [1, 4, 2], [1, 5, 2]]
    for c in xrange(len(cells)):
        fill_cell_with_text(document, cells[c], data[c])
    file = u'REQUISITION_REVIEW_TABLE_1.docx'
    application.ActiveDocument.SaveAs(file)
    application.ActiveDocument.Close()

    return
    #####################################
    # 合同评审表
    #####################################

    #####################################
    # 检验单
    #####################################
    file = u'VERIFICATION_SHEET.docx'
    path = dir + file

    ROW_COUNT = 1
    paper_pieces = items_count / ROW_COUNT

    for i in xrange(0, paper_pieces):
        document = application.Documents.Open(path)
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
        application.ActiveDocument.SaveAs(file)
        application.ActiveDocument.Close()

        #####################################
        # 设备验收表
        #####################################

        #####################################
        # 直发单
        #####################################

        #####################################
        # 设备卡
        #####################################


def fill_cell_with_text(document, position, text):
    table_seq = position[0]
    row_seq = position[1]
    col_seq = position[2]
    cell = document.Tables(table_seq).Cell(Row=row_seq, Column=col_seq)
    cell.Range.Text = text
