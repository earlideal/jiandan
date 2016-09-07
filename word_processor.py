# -*- coding: utf-8 -*-
import os

from win32com.client import Dispatch

word = Dispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
working_dir = os.getcwd() + u'\采购表格'
path = working_dir + '\\' + u'请购单.docx'
print path
doc = word.Documents.Open(path)
try:
    cell = doc.Tables(1).Cell(Row=1, Column=2)
    print cell.Range.Text.decode('utf-8').encode('gbk')
except:
    print "error!"
word.ActiveDocument.Save()
# word.ActiveDocument.PrintOut()
word.ActiveDocument.Close()
word.Quit()
