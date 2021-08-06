from subword.learn_bpe import main as learn_main
from subword.apply_bpe import BPE
import codecs


class SubwordProcessing:
    def __init__(self, data, input, output="./model", symbols=30000):
        self.inputFile = input
        self.outputFile = output
        self.data = data
        self.input = codecs.open(input, encoding='utf-8')
        self.output = codecs.open(output, 'w', encoding='utf-8')
        self.symbols = int(symbols)

    def learnBpe(self):
        try:
            learn_main(self.input, self.output, self.symbols)
            print("learn bpe processing compalte")
            return True
        except Exception as e:
            print("learn bpe processing fail :", e)
            return False

    def applyBpe(self):
        processedData = []
        codes = codecs.open(self.outputFile, encoding='utf-8')

        bpe = BPE(codes=codes, merges=-1, separator='▁',
                  vocab=None, glossaries=None)

        for data in self.data:
            line = data[1]
            leading_whitespace = len(line)-len(line.lstrip())
            if leading_whitespace:
                # args.output.write(line[:leading_whitespace])
                pass

            processedData.append([data[0], bpe.segment(line.strip())])

            trailing_whitespace = len(line)-len(line.rstrip())
            if trailing_whitespace:
                processedData.append([data[0], line[-trailing_whitespace:]])

        return processedData
