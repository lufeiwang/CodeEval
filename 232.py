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
            [l, rep] = test.split(' | ')
            l = l.split(' ')
            rep = int(rep)
            
            while rep != 0:
                for i,val in enumerate(l):
                    if i == 0:
                        next
                    elif int(val) < int(l[i-1]):
                        l[i] = l[i-1]
                        l[i-1] = val
                        break
                rep -= 1
            print ' '.join(l)