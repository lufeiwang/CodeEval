# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    translater=[('zero','0'),('one','1'),('two','2'),('three','3')
    ,('four','4'),('five','5'),('six','6'),('seven','7'),('eight','8'),
    ('nine','9')]
    d = dict(translater)
    
    with open(file_path,'r') as test_cases:
        for test in test_cases:
            test = test.rstrip('\n')
            words=test.split(';')
            print ''.join([d[word] for word in words])