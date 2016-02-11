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
           ang = float(test.rstrip('\n'))
           ans = str(int(ang)) + '.'
           mins = ang%1
           ans +='{0:0>2}'.format(int(mins * 60)) + "'"
           secs = mins * 60 % 1
           ans += '{0:0>2}'.format(int(secs * 60)) + '"'
           print ans