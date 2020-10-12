from textrenderer.corpus.corpus import Corpus
import numpy as np


class EngCorpus(Corpus):
    """
    Load English corpus by words, and get random {self.length} words as result
    """

    def load(self):
        self.load_corpus_path()

        for i, p in enumerate(self.corpus_path):
            print("Load {} th eng corpus".format(i))
            with open(p, encoding='utf-8') as f:
                data = f.read()

            lines = data.split('\n')
            for line in lines:
                for word in line.split(' '):
                    word = word.strip()
                    word = ''.join(filter(lambda x: x in self.charsets, word))

                    if word != u'':
                        self.corpus.append(word)
            print("Word count {}".format(len(self.corpus)))

    def get_sample(self, img_index):
        cnt = 0
        while True:
            if self.length == -1:
                length = np.random.randint(3, 5)
            start = np.random.randint(0, len(self.corpus) - length + 1)
            words = self.corpus[start:start + length]
            word = ' '.join(words)
            if len(word) > self.max_length:
                if cnt >= 10:
                    return word[:self.max_length]
                cnt += 1
                continue
            return word
