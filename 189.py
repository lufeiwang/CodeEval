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
            inp = test.rstrip('\n').split(' ')
            n,inp = inp[0],inp[1:]
            inp=map(int,inp)
            est = round(sum(inp) / int(n),0)
            ans = sum([abs(x - est) for x in inp])
            print '%.0f' %ans