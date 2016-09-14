# -*- coding: utf-8 -*-

from win32com.client import Dispatch

import to_be_filled


class WordProcessor(object):
    def __init__(self):
        super(WordProcessor, self).__init__()
        self.word_application = Dispatch('Word.Application')
        self.word_application.Visible = 1
        self.word_application.DisplayAlerts = 0

        self.generate_printing_files()

    def generate_printing_files(self):
        to_be_filled.fill_tables_with_content(self.word_application, u'请购单.docx', [1, 1, 2], u'极端环境量子物质中心')

    def quit_word(self):
        self.word_application.Quit()
