# -*- coding: utf-8 -*-
import os

from win32com.client import Dispatch


class WordProcessor(object):
    def __init__(self):
        super(WordProcessor, self).__init__()
        self.word = Dispatch('Word.Application')
        self.word.Visible = 1
        self.word.DisplayAlerts = 0

    def print_word(self):
        path = 'C:\\Users\\John\\Documents\\PYTHON\\jiandan\\templates\\'
        for file in os.listdir(path):
            print file.decode(encoding='gb2312')
            doc = self.word.Documents.Open(path + "\\" + file)
            word.ActiveDocument.Save()
            # word.ActiveDocument.PrintOut()
            self.word.ActiveDocument.Close()

    def quit_word(self):
        self.word.Quit()
