# -*- coding: utf-8 -*-
import os

from win32com.client import Dispatch

word = Dispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
appdir = os.getcwd() + u'\采购表格'
path = appdir + '\\' + u'请购单.docx'
print path

fill_table_with_content()

word.ActiveDocument.Save()
# word.ActiveDocument.PrintOut()
word.ActiveDocument.Close()
word.Quit()


def fill_table_with_content(position, content):
    if len(position) != 3:
        print u'表格需要用表、行、列三个坐标定位'
        return
    table = position[0]
    row = position[1]
    column = position[2]
    doc = word.Documents.Open(path)
    try:
        cell = doc.Tables(table).Cell(Row=row, Column=column)
        cell.Range.Text = content
    except:
        print u'在给表格数据赋值的时候发生错误。', [position]