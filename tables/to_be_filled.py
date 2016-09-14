# -*- coding: utf-8 -*-
import model


def fill_tables_with_content(application, file, position, content):
    path = 'C:\\Users\\John\\Documents\\PYTHON\\jiandan\\templates\\'
    path = path + file
    document = application.Documents.Open(path)
    table_seq = position[0]
    row_seq = position[1]
    col_seq = position[2]
    cell = document.Tables(table_seq).Cell(Row=row_seq, Column=col_seq)
    cell.Range.Text = content
    application.ActiveDocument.Save()
    t = cell.Range.Text

    application.Quit()


def fill_table_with_content(application, file):
    swift_code = '20160914215718'
    transaction = model.session.query(model.Transaction).filter_by(swift_code=swift_code).first()
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
    items = model.session.query(model.InventoryList).filter_by(swift_code=transaction.swift_code).all()
    print len(items)
