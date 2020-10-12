import os
import json

# province_name = '/Users/guoxiaolu/data/region_json/province.json'
# city_name = '/Users/guoxiaolu/data/region_json/city.json'
# county_name = '/Users/guoxiaolu/data/region_json/county.json'
# town_name = '/Users/guoxiaolu/data/region_json/town.json'

# pf = open(province_name, 'r')
# pdict = json.load(pf)
# pf.close()

# cf = open(city_name, 'r')
# cdict = json.load(cf)
# cf.close()

# cf1 = open(county_name, 'r')
# cdict1 = json.load(cf1)
# cf1.close()

# tf = open(town_name, 'r')
# tdict = json.load(tf)
# tf.close()

# province_list = []
# city_list = []
# county_list = []
# town_list = []

# ids = {}

# for v in pdict:
#     province_list.append(v['name'])
#     ids[v['id']] = v['name']

# for k, v in cdict.items():
#     for value in v:
#         if value['name'] == '市辖区':
#             ids[value['id']] = ids[k]
#         else:
#             ids[value['id']] = ids[k] + value['name']
#             city_list.append(ids[k] + value['name'])

# for k, v in cdict1.items():
#     for value in v:
#         if value['name'] == '市辖区':
#             ids[value['id']] = ids[k]
#         else:
#             ids[value['id']] = ids[k] + value['name']
#             county_list.append(ids[k] + value['name'])

# for k, v in tdict.items():
#     for value in v:
#         vname = value['name']
#         if '办事处' in vname:
#             vname = vname.replace('办事处', '')
#         ids[value['id']] = ids[k] + vname
#         town_list.append(ids[k] + vname)

# print(len(province_list), len(city_list), len(county_list), len(town_list))

# wname = './region.txt'
# wf = open(wname, 'w')
# for k, v in ids.items():
#     wf.write(v + '\n')
# wf.close()

# oname = '/Users/guoxiaolu/data/Company-Names-Corpus/Organization-Names-Corpus（110W）.txt'
# f = open(oname, 'r')
# lines = f.readlines()
# f.close()
# cnt = 0
# for line in lines:
#     if '北京市公安局海淀分局' in line:
#         cnt += 1
#         print(line)
# print(cnt)

import shutil
font_path = '/Users/guoxiaolu/data/fonts_master/ofl'
dst_path = '/Users/guoxiaolu/data/google_fonts'
names = os.listdir(font_path)
for name in names:
    fpath = os.path.join(font_path, name)
    if not os.path.isdir(fpath):
        continue
    fnames = os.listdir(fpath)
    for fname in fnames:
        extnames = os.path.splitext(fname)
        if extnames[1] != '.ttf':
            continue
        sname = os.path.join(fpath, fname)
        dname = os.path.join(dst_path, fname)
        shutil.copy(sname, dname)

# import shutil
# bj_path = '/Users/guoxiaolu/data/背景图'
# bg_path = '/Users/guoxiaolu/data/background'
# names = os.listdir(bj_path)
# cnt = 0
# for name in names:
#     fpath = os.path.join(bj_path, name)
#     if not os.path.isfile(fpath):
#         continue
#     cnt += 1
#     dname = os.path.join(bg_path, '%05d.png'%(cnt))
#     shutil.copy(fpath, dname)