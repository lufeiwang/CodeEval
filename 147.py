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
           inp = test.rstrip('\n')
           processed=[1 if i.isupper() else 0 for i in inp]
           print 'lowercase: {0:.2f} uppercase: {1:.2f}'.format((1.0 - float(sum(processed))/len(inp)) * 100,float(sum(processed))/len(inp) * 100)