# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path,'r') as test_cases:
        for test in test_cases:
            s,p= test.rstrip('\n').split(' ')
            print ''.join(x.upper() if y == '1' else x.lower() for (x,y) in zip(s,p))