import os
path = '/Users/guoxiaolu/work/code/text_renderer/synth_chn/labels/chn2_labels.txt'
wpath = '/Users/guoxiaolu/work/code/text_renderer/synth_chn/labels/new1.txt'
EN = u"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`"'"'_-~=+\|/()[]{}<>.,;:!^%#@$&?*¥"""
# EN = u"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"""
f = open(path, 'r')
lines = f.readlines()
f.close()
wf = open(wpath, 'w')
for line in lines:
    con = line.strip().split('\t')
    tmp = con[1].split(' ')
    label_with_space = []
    for lws in tmp:
        if len(lws) != 0:
            label_with_space.append(lws)
    slen = len(label_with_space)
    if len(label_with_space) == 1:
        wf.write(con[0] + '\t' + label_with_space[0] + '\n')
    else:
        marks = [0] * (slen - 1)
        for i in range(0, slen - 1):
            left = label_with_space[i][-1]
            right = label_with_space[i + 1][0]
            if left in EN or right in EN:
                marks[i] = 1
            else:
                pass
        wstr = label_with_space[0]
        for i, m in enumerate(marks):
            if m ==0:
                wstr += label_with_space[i + 1]
            else:
                wstr = wstr + ' ' + label_with_space[i + 1]
        wf.write(con[0] + '\t' + wstr + '\n')
wf.close()    