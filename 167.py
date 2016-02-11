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
           if len(inp) <= 55:
               print inp
           else:
               inp = inp[:40]
               try:
                   ind = inp.rindex(' ')
               except ValueError:
                   ind = 40
               print inp[:ind] + '... <Read More>'
             
            
           