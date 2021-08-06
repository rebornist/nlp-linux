#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from outputData import OutputData, OutputTsv, OutputText, OutputExcel, OutputTrainData
from refineData import DataRefiner
from tokenizeData import DataTokenizer
from subwordApi import SubwordProcessing
from detokenizeData import Detokenizer
from pytorchApi import TorchtextLoader

if __name__ == '__main__':

    if sys.argv[1] == "none":
        filepath = './all_files_data_210708.xlsx'
    else:
        filepath = sys.argv[1]

    output = OutputData(filepath, int(sys.argv[2]) - 1, int(sys.argv[3]) - 1)
    dataOrg = output.returnData()
    filename = output.returnPath()
    OutputTsv(dataOrg, filename)

    dataRefine = DataRefiner(dataOrg).dataPreprocess()
    refinedFilename = f'{filename}.ref'
    OutputTsv(dataRefine, refinedFilename)

    dt = DataTokenizer(dataRefine)
    dataTokenize = dt.dataProcessing()
    tokenizedFilename = f'{refinedFilename}.tok'
    OutputTsv(dataTokenize, tokenizedFilename)

    data_blank = dt.tokenize_str_to_blank()
    tokenize_to_blank_filename = f'{tokenizedFilename}.blank'
    OutputTsv(data_blank, tokenize_to_blank_filename)

    # txt = OutputText(dataTokenize, tokenizedFilename)
    # txt.resetData()

    # sw = SubwordProcessing(dataTokenize, f'{tokenizedFilename}.text')
    # resp = sw.learnBpe()
    # if resp:
    # ds = sw.applyBpe()
    dts = Detokenizer(dataTokenize).detokenize()
    detokenizedFilename = f'{tokenizedFilename}.detok'
    OutputTsv(dts, detokenizedFilename)
    # OutputTrainData(dts, detokenizedFilename, 157260)
    # OutputExcel(dts, detokenizedFilename)

    ttl = TorchtextLoader(f'{tokenize_to_blank_filename}.tsv')
    ttl.getMiniBatch()
    ttl.useVocab()
    fws = ttl.output_frequent_words()
    frequentFilename = 'output/frequent_words'
    OutputTsv(fws, frequentFilename)

    mb = ttl.output_mini_batch()
    minibatchFilename = f'{tokenize_to_blank_filename}.batch'
    OutputTsv(mb, minibatchFilename)