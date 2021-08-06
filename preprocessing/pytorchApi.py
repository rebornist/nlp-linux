from torch_txt.data_loader import DataLoader


class TorchtextLoader:
    def __init__(self, filename):
        self.filename = filename
        self.loaders = DataLoader(
            train_fn=self.filename,
            batch_size=999999,
            valid_ratio=.2,
            device=-1,
            max_vocab=999999,
            min_freq=5,
        )

    def getMiniBatch(self):
        # Get mini-batch tensors
        self.data = next(iter(self.loaders.train_loader))

    def useVocab(self):
        self.vocab = self.loaders.text.vocab

    def output_frequent_words(self):
        frequent_words = []
        for word in self.loaders.text.vocab.itos:
            frequent_words.append([word, self.loaders.text.vocab.freqs[word]])
        
        return frequent_words

    def output_mini_batch(self):
        output_datas = []
        for x in self.data.text:
            line = []
            for x_i in x:
                line += [self.loaders.text.vocab.itos[x_i]]
            output_datas.append(''.join(line))
        
        return output_datas

