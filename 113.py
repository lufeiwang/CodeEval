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
           l1,l2 = test.rstrip('\n').split(' | ')
           l1 = l1.split(' ')
           l2 = l2.split(' ')
           print ' '.join([str(int(n1) * int(n2)) for n1, n2 in zip(l1,l2)])