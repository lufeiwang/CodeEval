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
            words = test.rstrip('\n')
            ans = words[0]
            for ind in range(1,len(words)):
                if words[ind] != words[ind-1]:
                    ans += words[ind]
            print ''.join(ans)
            