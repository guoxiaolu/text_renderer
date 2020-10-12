from textrenderer.corpus.corpus import Corpus
import numpy as np


class ListCorpus(Corpus):
    """
    get_sample from corpus line by line
    """

    def load(self):
        self.load_corpus_path()

        for i, p in enumerate(self.corpus_path):
            print("Load corpus: %s" % p)
            with open(p, encoding='utf-8') as f:
                lines = f.readlines()

            for line in lines:
                con = line.strip()
                if len(con) > self.max_length:
                    print ('too long text:%s'%(con))
                    continue
                is_mark = False
                for c in con:
                    if c not in self.charsets:
                        is_mark = True
                        break
                if not is_mark:
                    self.corpus.append(line.strip())
                else:
                    print ('unstandard word:%s,text:%s'%(c, con))

        print("Total lines: {}".format(len(self.corpus)))

    def get_sample(self, img_index):
        index = img_index % len(self.corpus)
        return self.corpus[index]
