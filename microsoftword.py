# -*- coding: utf-8 -*-

from win32com.client import Dispatch


class WordSheetsHandler(object):
    def __init__(self):
        super(WordSheetsHandler, self).__init__()
        self.application = Dispatch('Word.Application')
        self.application.Visible = 1
        self.application.DisplayAlerts = 0
