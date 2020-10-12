import os
from tqdm import tqdm
lpath = '/Users/guoxiaolu/work/code/text_renderer/output/data/labels_new.txt'
f = open(lpath, 'r')
lines = f.readlines()
f.close()
names = []
for line in tqdm(lines):
    con = line.strip().split('\t')
    name = con[0]
    if name in names:
        print (name)
    else:
        names.append(name)