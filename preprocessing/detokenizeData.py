import sys


class Detokenizer:
    def __init__(self, data):
        self.data = data

    def detokenize(self):
        outputs = []
        for data in self.data:
            line = data[1]
            if line.strip() != "":
                line = line.strip().replace('▁▁', ' ').replace('▁', '').strip()
                outputs.append([data[0], line])

        return outputs
