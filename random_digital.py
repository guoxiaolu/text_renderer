import os
import random
import numpy as np
from tqdm import tqdm
number = 50000
type = ['money', 'contract_number']
btype = [False, True]
wpath = './number.txt'
wf = open(wpath, 'w')
for i in tqdm(range(0, number)):
    rtype = random.choice(type)
    if rtype == 'money':
        is_comma = random.choice(btype)
        is_float = random.choice(btype)
        money = ['', '€', '£', '$', '¥']
        rdigital = random.uniform(0.001, 100000000)
        if is_float:
            fint = random.choice([1, 2, 3])
            rdigital = round(rdigital, fint)
        else:
            rdigital = int(rdigital)
        if is_comma:
            r = format(rdigital, ',')
        else:
            r = format(rdigital)
        rm = random.choice(money)
        rstr = rm + r
        # print(rm+r)
    elif rtype == 'contract_number':
        alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        number = '0123456789'
        seperate = ['', '-', '/', '\\']
        # sep_num = random.randint(1, 3)
        rlen = random.randint(8, 16)
        ralen = random.randint(1, 5)
        idxs = np.random.randint(0, len(alphabet), size=ralen)
        astr = ''.join([alphabet[i] for i in idxs])
        idxs = np.random.randint(0, len(number), size=rlen - ralen)
        nstr = ''.join([number[i] for i in idxs])
        rs = random.choice(seperate)
        rstr = astr + rs + nstr
        # print(rstr)
    wf.write(rstr + '\n')
wf.close()