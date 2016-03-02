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
            seq = test.rstrip('\n').split(' ')
            curr_n = seq[0]
            curr_counter = 0
            ans = []
            for i in seq:
                if i == curr_n:
                    curr_counter += 1
                else:
                    ans.extend([str(curr_counter), curr_n])
                    curr_n = i
                    curr_counter = 1
            ans.extend([str(curr_counter), curr_n])
            print ' '.join(ans)
