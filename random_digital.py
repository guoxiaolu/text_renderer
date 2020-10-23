import os
import random
import numpy as np
import cn2an
from tqdm import tqdm

if __name__ == '__main__':
    number = 10000
    # type = ['money', 'contract_number', 'chinese']
    type = ['chinese']
    btype = [False, True]
    wpath = './number_chinese.txt'
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
        elif rtype == 'chinese':
            is_float = random.choice(btype)
            rdigital = random.uniform(0.001, 100000)
            if is_float:
                fint = random.choice([1, 2, 3])
                rdigital = round(rdigital, fint)
            else:
                rdigital = int(rdigital)
            rstr = cn2an.an2cn(rdigital, "rmb")
            # rstr = digital_to_chinese(rdigital)
        wf.write(rstr + '\n')
    wf.close()