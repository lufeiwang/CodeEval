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
            inp = map(int,test.rstrip('\n').split(' '))
            inp = map(int, inp)
            n,inp = inp[0],inp[1:]
            ans=min(sum(abs(x - j) for x in inp) for j in range(1,max(inp)+1))
            print '%.0f' %ans