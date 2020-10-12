import os
import shutil
from tqdm import tqdm
path = '/Users/guoxiaolu/work/code/text_renderer/output_chn1/default'
dst_path = '/Users/guoxiaolu/work/code/text_renderer/synth_chinese/images'
names = os.listdir(path)
for name in tqdm(names):
    absname = os.path.join(path, name)
    dstname = os.path.join(dst_path, name)
    if os.path.isfile(dstname):
        print (name)
    shutil.copy(absname, dstname)