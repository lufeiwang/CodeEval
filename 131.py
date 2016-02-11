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
            test = test.rstrip('\n')
            num, pattern = test.split(' ')
            try:
                ind=pattern.index('-')
                op = -1
            except ValueError:
                ind=pattern.index('+')
                op = 1
            print str(int(num[:ind]) + op * int(num[ind:]))