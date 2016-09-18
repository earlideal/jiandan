# -*- coding: utf-8 -*-
import model


def disassemble_word_tables(application, file):
    path = 'C:\\Users\\John\\Documents\\PYTHON\\jiandan\\templates\\'
    path = path + file
    document = application.Documents.Open(path)

    demo_swift_code = '20160914225507'

    transaction = model.session.query(model.Transaction).filter_by(swift_code=demo_swift_code).first()
    requisition = transaction.requisition
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


def fill_table_cell(document, position, text):
    table_seq = position[0]
    row_seq = position[1]
    col_seq = position[2]
    cell = document.Tables(table_seq).Cell(Row=row_seq, Column=col_seq)
    cell.Range.Text = text


def list_all_inventories():
    transaction = model.session.query(model.Transaction).filter_by(swift_code=swift_code).first()
    items = model.session.query(model.Inventory).filter_by(swift_code=transaction.swift_code).all()
    print len(items)
