# -*- coding: utf-8 -*-

def qingou():
    print u'请购单'


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
    print t
    application.Quit()
