# -*- coding: utf-8 -*-
import os
import time
from win32com.client import Dispatch

word = Dispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
path = 'C:\\Users\\John\\Documents\\PYTHON\\jiandan\\templates\\'
for file in os.listdir(path):
    print file.decode(encoding='gb2312')
    doc = word.Documents.Open(path + "\\" + file)
    word.ActiveDocument.Save()
    # word.ActiveDocument.PrintOut()
    word.ActiveDocument.Close()
word.Quit()
class WordProcessor(object):
    def __init__(self):
        super(WordProcessor, self).__init__()
