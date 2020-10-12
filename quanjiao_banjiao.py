#!/usr/env/bin python3
import os
quanjiao = u"""ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０｀”’“‘＿－～＝＋＼｜／（）［］｛｝＜＞．，；：！＾％＃＠＄＆？＊￥"""
banjiao = u"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`"'"'_-~=+\|/()[]{}<>.,;:!^%#@$&?*¥"""
lianjie = '─-_ '
src = '/Users/guoxiaolu/data/语料_sentence'
dst = '/Users/guoxiaolu/data/语料_sentence1'
if not os.path.exists(dst):
    os.mkdir(dst)
names = os.listdir(src)
for name in names:
    if name[0] == '.':
        continue
    print (name)
    absname = os.path.join(src, name)
    dstname = os.path.join(dst, name)
    wf = open(dstname, 'w', encoding='utf-8')
    f = open(absname, 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        nline = ''
        for c in line:
            if c in quanjiao:
                idx = quanjiao.index(c)
                bj = banjiao[idx]
                nline += bj
            else:
                nline += c
        # lianjie
        nnline = ''
        mark = ''
        for c in nline:
            if c in lianjie and mark != c:
                mark = c
                nnline += c
            elif c in lianjie and mark == c:
                pass
            elif c not in lianjie and mark in lianjie:
                mark = ''
                nnline += c
            else:
                nnline += c 
        wf.write(nnline)
    wf.close()
    
