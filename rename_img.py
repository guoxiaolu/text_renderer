import os
from tqdm import tqdm
from PIL import Image
lpath = '/Users/guoxiaolu/work/code/text_renderer/output_chn2/default/tmp_labels.txt'
wpath = '/Users/guoxiaolu/work/code/text_renderer/output_chn2/default/chn2_labels.txt'
img_path = '/Users/guoxiaolu/work/code/text_renderer/output_chn2/default'
f = open(lpath, 'r')
lines = f.readlines()
f.close()
wf = open(wpath, 'w')
for line in tqdm(lines):
    con = line.strip().split(' ')
    label = con[1]
    if len(con) > 2:
        for c in con[2:]:
            nstr = ' ' + c
            label += nstr
    absname = os.path.join(img_path, con[0] + '.jpg')
    if not os.path.isfile(absname):
        continue
        # absname = os.path.join(img_path, 'entity_' + con[0] + '.jpg')
        # if not os.path.isfile(absname):
        #     absname = os.path.join(img_path, 'number_' + con[0] + '.jpg')
        #     if not os.path.isfile(absname):
        #         continue
    nname = 'chn2_' + con[0] + '.jpg'
    dstname = os.path.join(img_path, nname)
    # if not os.path.isfile(dstname):
    #     os.rename(absname, dstname)
    os.rename(absname, dstname)
    wstr = '%s\t%s\n'%(nname, label)
    wf.write(wstr)
wf.close()


# lpath = '/Users/guoxiaolu/work/code/text_renderer/output/en1/tmp_labels.txt'
# wpath = '/Users/guoxiaolu/work/code/text_renderer/output/en1_labels.txt'
# f = open(lpath, 'r')
# lines = f.readlines()
# f.close()
# wf = open(wpath, 'w')
# for line in tqdm(lines):
#     con = line.strip().split(' ')
#     nname = 'en1_' + con[0] + '.jpg'
#     label = con[1]
#     if len(con) > 2:
#         for c in con[2:]:
#             nstr = ' ' + c
#             label += nstr
#     wstr = '%s\t%s\n'%(nname, label)
#     wf.write(wstr)
# wf.close()

