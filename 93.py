# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys
import re

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path,'r') as test_cases:
        for test in test_cases:
            test = test.rstrip('\n')
            p = re.compile('[^0-9]')
            distances=[int(d) for d in p.split(test) if d != '']
            distances.sort()
            
            ans_partial = [str(val - distances[i-1]) for i,val in enumerate(distances) if i != 0]           
            ans = [str(distances[0])]
            ans.extend(ans_partial)

            print ','.join(ans)