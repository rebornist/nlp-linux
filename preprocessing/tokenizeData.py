#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
from konlpy.tag import Mecab
from outputData import OutputData, OutputTsv
from refineData import DataRefiner


class DataTokenizer:
    def __init__(self, data):
        self.data = data
        self.tokenized = []
        self.mecab = Mecab()

    def dataProcessing(self):
        for i in self.data:
            tokenizedTxt = self.dataTokenize(i[1])
            cleaningText = self.textCleaning(tokenizedTxt)
            self.tokenized.append([i[0], cleaningText])

        return self.tokenized

    def mecabMorphs(self, text):
        tokenizedText = self.mecab.morphs(text)

        buf = []
        STR = '▁'

        for txt in tokenizedText:
            buf.append(f'{STR}{txt}')

        return ''.join(buf)

    def dataTokenize(self, text):
        splitedText = text.split(' ')

        tmp_buf = []

        # We assume that stdin has more tokens than reference input.
        for txt in splitedText:
            tokenizedText = self.mecabMorphs(txt)
            tmp_buf.append(tokenizedText)

        return ' '.join(tmp_buf)

    def textCleaning(self, text):
        # 문자와 숫자를 제외한 글자를 제거하는 함수.
        # doc = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", text)
        items = []
        doc = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z▁ ]", "", text)
        for value in doc.split(' '):
            if value != "":
                items.append(value)

        return ' '.join(items)

    def tokenize_str_to_blank(self):
        blank_texts = []
        for tok in self.tokenized:
            text = f'{tok[1]}'.replace('▁', ' ', -1)
            blank_texts.append([tok[0], text])

        return blank_texts



# if __name__ == '__main__':

#     if sys.argv[1] == "none":
#         filepath = r"C:\Users\saint\OneDrive\proj\2021\sen\04.대상자료\all_files_data_210708.xlsx"
#     else:
#         filepath = sys.argv[1]

#     output = OutputData(filepath, int(sys.argv[2]) - 1, int(sys.argv[3]) - 1)
#     dataOrg = output.returnData()
#     filename = output.returnPath()
#     OutputTsv(dataOrg, filename)

#     dataRefine = DataRefiner(dataOrg).dataPreprocess()
#     refinedFilename = f'{filename}.refined'
#     OutputTsv(dataRefine, refinedFilename)

#     dataTokenize = DataTokenizer(dataRefine).dataProcessing()
#     tokenizedFilename = f'{refinedFilename}.tokenized'
#     OutputTsv(dataTokenize, tokenizedFilename)
