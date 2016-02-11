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
            words = test.split(' ')
            pairs = zip([int(len(word)) for word in words],words)
            pairs.sort(key=lambda x: x[0], reverse=True)
            print pairs[0][1]
            