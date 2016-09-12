# -*- coding: utf-8 -*-

from win32com.client import Dispatch

word = Dispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
path = 'C:\\Users\\John\\PycharmProjects\\jiandan\\templates\\' + '请购单.docx'
print path
doc = word.Documents.Open(path)
word.ActiveDocument.Save()
word.ActiveDocument.PrintOut()
word.ActiveDocument.Close()
word.Quit()
