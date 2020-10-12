import os
from tqdm import tqdm
from PIL import Image

WIDTH_TH = 280

path = '/Users/guoxiaolu/work/code/text_renderer/synth_chn/images'
labels_path = '/Users/guoxiaolu/work/code/text_renderer/synth_chn/labels/all.txt'
wpath = '/Users/guoxiaolu/work/code/text_renderer/synth_chn/labels/all_new.txt'
wf = open(wpath, 'w')
f = open(labels_path, 'r')
lines = f.readlines()
f.close()
for line in tqdm(lines):
    con = line.strip().split('\t')
    absname = os.path.join(path, con[0])
    if not os.path.isfile(absname):
        print (con[0])
        continue
    try:
        img = Image.open(absname).convert('L')
        if img.height != 32 or img.width > WIDTH_TH:
            print(con[0])
            continue
    except Exception as e:
        print (con[0])
        continue
    wf.write(line)
wf.close()