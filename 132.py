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
            nums = test.rstrip('\n').split(',')
            d={}
            for i in nums:
                if d.get(i) == None:
                    d[i] = 1
                else:
                    d[i] += 1 
            t = max(d.iteritems(),key=lambda x: x[1])
            if t[1] >= len(nums) / 2:
                print t[0]
            else:
                print 'None'