import os
from tqdm import tqdm
cpath = '/Users/guoxiaolu/data/待定/char_std_5990.txt'
f = open(cpath, 'r')
lines = f.readlines()
f.close()
stmp = [line.strip() for line in lines]
charset = ' '.join(stmp)


# dpath = '/Users/guoxiaolu/data/待定/small'
# dnames = os.listdir(dpath)
# wpath = '/Users/guoxiaolu/data/待定/sentence_finnews.txt'
# wf = open(wpath, 'w')
# for dname in tqdm(dnames):
#     path = os.path.join(dpath, dname)
#     f = open(path, 'r')
#     lines = f.readlines()[1:]
#     f.close()
#     # name = os.path.splitext(os.path.basename(path))[0]

#     cnt = 0
#     for line in tqdm(lines):
#         con = line.strip().split(',')
#         if len(con) == 1:
#             text = con[0]
#         elif len(con) == 3:
#             text = con[2]
#         else:
#             continue
#         # if '#' in text or '?' in text or '*' in text or '{IMG' in text or '上页' in text or ';;' in text or '！！' in text or '@' in text or 'nbsp' in text or '＊' in text or 'KB' in text or len(text) < 20 or '<' in text or 'function' in text or '>>' in text or 'copyrightdedecms' in text or text[0] == ';':
#         #     continue
#         if '{IMG' in text or ';;' in text or '！！' in text or  'nbsp' in text or len(text) < 20 or 'copyrightdedecms' in text or text[0] == ';':
#             continue
#         if '《' in text and '》'not in text:
#             continue
#         if '《' not in text and '》'in text:
#             continue
#         if '（'in text and '）' not in text:
#             continue
#         if '（'not in text and '）' in text:
#             continue
#         is_mark = False
#         for t in text:
#             if t not in charset:
#                 is_mark = True
#                 break
#         if is_mark:
#             cnt += 1
#             continue
#         wf.write(text+'\n')
#     print(cnt)
# wf.close()


# path = '/Users/guoxiaolu/data/待定/corpus'
# wpath = '/Users/guoxiaolu/data/待定/sentence_fincorpus.txt'
# wf = open(wpath, 'w')

# f = open(path, 'r')
# lines = f.readlines()[1:]
# f.close()
# # name = os.path.splitext(os.path.basename(path))[0]

# cnt = 0
# for line in tqdm(lines):
#     con = line.strip().split(',')
#     if len(con) == 1:
#         text = con[0]
#     elif len(con) == 3:
#         text = con[2]
#     else:
#         continue
#     # if '#' in text or '?' in text or '*' in text or '{IMG' in text or '上页' in text or ';;' in text or '！！' in text or '@' in text or 'nbsp' in text or '＊' in text or 'KB' in text or len(text) < 20 or '<' in text or 'function' in text or '>>' in text or 'copyrightdedecms' in text or text[0] == ';':
#     #     continue
#     if '{IMG' in text or '上页' in text or ';;' in text or '！！' in text or  'nbsp' in text or 'KB' in text or len(text) < 20  or 'function' in text  or 'copyrightdedecms' in text or text[0] == ';':
#         continue
#     if '《' in text and '》'not in text:
#         continue
#     if '《' not in text and '》'in text:
#         continue
#     if '（'in text and '）' not in text:
#         continue
#     if '（'not in text and '）' in text:
#         continue
#     is_mark = False
#     for t in text:
#         if t not in charset:
#             is_mark = True
#             break
#     if is_mark:
#         cnt += 1
#         continue
#     wf.write(text+'\n')
# print(cnt)
# wf.close()




# path = '/Users/guoxiaolu/data/待定/nonghangzhidao_filter.csv'
# wpath = '/Users/guoxiaolu/data/待定/sentence_nonghangzhidao.txt'
# wf = open(wpath, 'w')

# f = open(path, 'r')
# lines = f.readlines()[1:]
# f.close()
# # name = os.path.splitext(os.path.basename(path))[0]

# cnt = 0
# nline = []
# for line in tqdm(lines):
#     con = line.strip().split(',')
#     if len(con) != 4:
#         continue
#     text = con[2]
#     if int(con[-1]) != 1:
#         continue
#     if '#' in text or '*' in text or '{IMG' in text or '上页' in text or ';;' in text or '！！' in text or '@' in text or 'nbsp' in text or '＊' in text or 'KB' in text or len(text) < 20 or '<' in text or 'function' in text or '>>' in text or 'copyrightdedecms' in text or text[0] == ';':
#         continue
#     if '《' in text and '》'not in text:
#         continue
#     if '《' not in text and '》'in text:
#         continue
#     if '（'in text and '）' not in text:
#         continue
#     if '（'not in text and '）' in text:
#         continue
#     is_mark = False
#     for t in text:
#         if t not in charset:
#             is_mark = True
#             break
#     if is_mark:
#         cnt += 1
#         continue
#     if text in nline:
#         continue
#     nline.append(text)
#     wf.write(text+'\n')
# print(cnt)
# wf.close()

# xinhua
# import json
# path = '/Users/guoxiaolu/data/待定/chinese-xinhua-master/data/ci.json'
# f = open(path, 'r')
# jdict = json.load(f)
# f.close()
# word_path = '/Users/guoxiaolu/data/待定/语料/word_xinhua.txt'
# wf = open(word_path, 'w')
# explanation_path = '/Users/guoxiaolu/data/待定/语料/explanation_xinhua.txt'
# ef = open(explanation_path, 'w')
# for v in jdict:
#     ci = v['ci']
#     exp = v['explanation']
#     wf.write(ci + '\n')
#     cons = exp.split('\n')
#     for i, con in enumerate(cons):
#         ncon = con.replace('%d.'%(i+1),'')
#         ef.write(ncon + '\n')

# ef.close()
# wf.close()

# f = open('/Users/guoxiaolu/work/code/text_renderer/data/chars/chn.txt')
# lines = f.readlines()
# f.close()
# f = open('/Users/guoxiaolu/work/code/text_renderer/data/chars/char_std_5990.txt')
# clines = f.readlines()
# f.close()
# chars = [line.strip()for line in lines]
# cchars = [line.strip()for line in clines]
# cnt = 0
# clist = []
# for c in cchars:
#     if c in chars:
#         continue
#     cnt += 1
#     clist.append(c)
# print (cnt)
# print (clist)

# #上标下标，各种编号，数字英文加连接符，下划线很多，数字中间逗号小数点，日期，金额，H58-1/02
# comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:;!?-/()#*@=+&%><"\' $￥€£☑☐☒■√'
# charset_path = '/Users/guoxiaolu/work/code/text_renderer/data/chars/char_std_5990.txt'
# f = open(charset_path, 'r')
# lines = f.readlines()
# f.close()
# clist = []
# for line in lines:
#     clist.append(line.strip())
# for c in comp:
#     if c not in clist:
#         print(c)

# path = '/Users/guoxiaolu/data/语料_entity/购房合同.txt'
# wpath = '/Users/guoxiaolu/data/语料_entity/new.txt'
# wf = open(wpath, 'w')
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         con = line.strip()
#         con = con.replace('\t', '').replace(' ', '')
#         if con is '':
#             continue
#         if con[0] == '□':
#             ncon = '☑' + con[1:]
#             wf.write(ncon+'\n')
#             ncon = '√' + con[1:]
#             wf.write(ncon+'\n')
#         elif con[0] not in '☑√' and con[0] != '*' :
#             ncon = '*' + con
#             wf.write(ncon+'\n')

# # combine file
# path = '/Users/guoxiaolu/data/语料_sentence/English'
# wpath = '/Users/guoxiaolu/data/语料_sentence/English.txt'
# wf = open(wpath, 'w')
# names = os.listdir(path)
# for name in names:
#     exts = os.path.splitext(name)
#     if exts[1] != '.txt':
#         continue
#     absname = os.path.join(path, name)
#     f = open(absname, 'r')
#     lines = f.readlines()
#     f.close()
#     for line in lines:
#         if len(line) <= 20 or ' 'not in line:
#             continue
#         wf.write(line)
# wf.close()

# pname = '/Users/guoxiaolu/work/code/text_renderer/output/default/tmp_labels.txt'
# path = '/Users/guoxiaolu/work/code/text_renderer/output/default'
# f = open(pname, 'r')
# lines = f.readlines()
# f.close()
# names = os.listdir(path)
# print(len(names))
# for line in lines:

def sort_labels(tmp_label_fname, label_fname):
    lines = []
    with open(tmp_label_fname, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = sorted(lines)
    with open(label_fname, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line[9:])

sort_labels('/Users/guoxiaolu/work/code/text_renderer/output/default/tmp_labels.txt', '/Users/guoxiaolu/work/code/text_renderer/output/default/labels.txt')