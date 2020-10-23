import random
import numpy as np

from textrenderer.corpus.corpus import Corpus

EN = u"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"""
class LowCorpus(Corpus):
    def load(self):
        """
        Load one corpus file as one line , and get random {self.length} words as result
        """
        f = open(self.distribute_file, 'r')
        lines = f.readlines()
        f.close()
        distribute = {}
        for line in lines:
            if line[-1] == '\n':
                con = line[:-1].split('\t')
            else:
                con = line.split('\t')
            distribute[con[0]] = int(con[1])
        self.load_corpus_path()

        for i, p in enumerate(self.corpus_path):
            print_end = '\n' if i == len(self.corpus_path) - 1 else '\r'
            print("Loading chn corpus: {}/{}".format(i + 1, len(self.corpus_path)), end=print_end)
            with open(p, encoding='utf-8') as f:
                data = f.readlines()

            for line in data:
                line_striped = line.strip()
                line_striped = line_striped.replace('\u3000', '')
                line_striped = line_striped.replace('&nbsp', '')
                line_striped = line_striped.replace("\00", "")
                
                nline = ''.join(filter(lambda x: x in self.charsets, line_striped))
                nline_nouse_space = ''
                tmp = nline.split(' ')
                label_with_space = []
                for lws in tmp:
                    if len(lws) != 0:
                        label_with_space.append(lws)
                slen = len(label_with_space)
                if len(label_with_space) == 1:
                    nline_nouse_space = label_with_space[0]
                elif len(label_with_space) == 0:
                    continue
                else:
                    marks = [0] * (slen - 1)
                    for i in range(0, slen - 1):
                        left = label_with_space[i][-1]
                        right = label_with_space[i + 1][0]
                        if left in EN or right in EN:
                            marks[i] = 1
                        else:
                            pass
                    nline_nouse_space = label_with_space[0]
                    for i, m in enumerate(marks):
                        if m ==0:
                            nline_nouse_space += label_with_space[i + 1]
                        else:
                            nline_nouse_space = nline_nouse_space + ' ' + label_with_space[i + 1]
                  
                for k, c in enumerate(nline_nouse_space):
                    if c in distribute and distribute[c] < 1000:
                        idx = k
                        random_len = random.randint(10, self.max_length)
                        start = random.randint(max(idx - random_len, 0), idx)
                        end = min(start + random_len, len(nline_nouse_space) - 1)
                        if end - start != random_len:
                            start = max(end - random_len, 0)
                        rand_str = nline_nouse_space[start:start + random_len]
                        self.corpus.append(rand_str)

    def get_sample(self, img_index):
        index = img_index % len(self.corpus)
        return self.corpus[index]
