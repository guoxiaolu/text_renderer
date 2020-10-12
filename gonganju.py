import json
city_path = '/Users/guoxiaolu/data/region_json/city.json'
f = open(city_path, 'r')
city_dict = json.load(f)
f.close()
county_path = '/Users/guoxiaolu/data/region_json/county.json'
f = open(county_path, 'r')
county_dict = json.load(f)
f.close()
city = {}
for k, v in city_dict.items():
    if len(v) == 1:
        city[v[0]['id']] = v[0]['province']
    else:
        for v0 in v:
            city[v0['id']] = v0['name']
county = {}
for k, v in county_dict.items():
    ccounty = []
    for v0 in v:
        # if v0['name'] == '市辖区':
        #     continue
        ccounty.append(v0['name'])
    county[k] = ccounty

wpath = '/Users/guoxiaolu/data/语料/policestation1.txt'
wf = open(wpath, 'w')

for k, v in city.items():
    tstr = '%s公安局'%(v)
    wf.write(tstr + '\n')
    # if k not in county:
    #     tstr = '%s公安局'%(v)
    #     wf.write(tstr + '\n')
    #     continue
    # ccounty = county[k]
    # for cv in ccounty:
    #     if '市辖' in cv:
    #         continue
    #     elif cv[-1] == '区':
    #         if v in cv:
    #             nv = v.replace(v, '')
    #             tstr = '%s公安局%s分局'%(v, nv)
    #         elif v[:-1] in cv:
    #             nv = cv.replace(v[:-1], '')
    #             tstr = '%s公安局%s分局'%(v, nv)
    #         else:
    #             tstr = '%s公安局%s分局'%(v, cv[:-1])
    #     else:
    #         tstr = '%s公安局'%(cv)
    #     wf.write(tstr + '\n')
wf.close()