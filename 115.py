# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys
import re

if __name__ == '__main__':
    file_path = sys.argv[1]
    p1 = re.compile('[0-9,]+')
    p2 = re.compile('[a-z,]+',flags=re.IGNORECASE)
    with open(file_path,'r') as test_cases:
        for test in test_cases:
           inp = test.rstrip('\n')
           words = ','.join([i for i in re.split(p1,inp) if i])
           nums = ','.join([i for i in re.split(p2,inp) if i])
           print '|'.join(i for i in [words,nums] if i)