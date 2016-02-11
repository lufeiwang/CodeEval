# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys
import re

if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path,'r') as test_cases:
        for test in test_cases:
            test = test.rstrip('\n')
            pat = re.compile('[^a-j0-9]+')
            valid_chars=[i for i in pat.split(test) if len(i) != 0]
            if len(valid_chars) == 0:
                print 'NONE'
            else:
                print ''.join([str(ord(c)-97) if c.isalpha() else str(c) for c_l in valid_chars for c in c_l])