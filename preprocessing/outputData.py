import csv
import codecs
import openpyxl
import os


class ExcelReader:
    def __init__(self):
        self.readExcel()
        self.getData()

    def readExcel(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.ws = self.wb.active

    def getData(self):
        cnt = 0
        for data in self.ws.rows:
            if cnt > 0 and data[self.outputNumber].value:
                self.outputData.append([
                    data[self.indexNumber].value, data[self.outputNumber].value])
            cnt += 1
        else:
            self.wb.close()


class OutputData(ExcelReader):
    def __init__(self, filename, indexNumber, outputNumber):
        self.filename = filename
        self.indexNumber = indexNumber
        self.outputNumber = outputNumber
        self.outputData = []
        self.outputName = f'output/output'
        ExcelReader.__init__(self)

    def returnData(self):
        return self.outputData

    def returnPath(self):
        return self.outputName


class OutputTsv:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        self.dataOutput()
        self.resetData()
        print(f'{filename}`s create complate | total length is {len(data)}')

    def dataOutput(self):
        self.outFile = open(
            f'./{self.filename}.tsv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(self.outFile, delimiter='\t')
        writer.writerows([value for value in self.data])
        self.outFile.close()

    def resetData(self):
        self.data = []
        self.filename = ""


class OutputText:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        self.outputFilename = ""
        self.dataOutput()
        print(f'{filename}`s create complate | total length is {len(data)}')

    def dataOutput(self):
        self.outputFilename = f'./{self.filename}.text'
        output = codecs.open(self.outputFilename, 'w', encoding='utf-8')
        for data in self.data:
            output.write(data[1]+'\n')
        output.close()

    def resetData(self):
        os.remove(self.outputFilename)
        self.data = []
        self.filename = ""
        self.outputFilename = ""


class OutputExcel:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        self.dataOutput()
        self.resetData()
        print(f'{filename}`s create complate | total length is {len(data)}')

    def dataOutput(self):
        filename = f'./{self.filename}.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active

        for data in self.data:
            ws.append(data)

        wb.save(filename)
        wb.close()

    def resetData(self):
        self.data = []
        self.filename = ""


class OutputTrainData:
    def __init__(self, data, filename, cutNumber):
        self.data = data
        self.filename = filename
        self.cutNumber = int(cutNumber)
        self.dataOutput()
        self.resetData()
        print(
            f'{filename}.train & {filename}.test`s create complate | total length is {len(data)}')

    def dataOutput(self):
        trainFile = f'./{self.filename}.train'
        outTrainFile = open(
            f'./{trainFile}.tsv', 'w', newline='', encoding='utf-8')
        trainWriter = csv.writer(outTrainFile, delimiter='\t')
        trainWriter.writerows([value for value in self.data[:self.cutNumber]])
        outTrainFile.close()

        testFile = f'./{self.filename}.test'
        outTestFile = open(
            f'./{testFile}.tsv', 'w', newline='', encoding='utf-8')
        testWriter = csv.writer(outTestFile, delimiter='\t')
        testWriter.writerows([value for value in self.data[self.cutNumber:]])
        outTestFile.close()

    def resetData(self):
        self.data = []
        self.filename = ""
