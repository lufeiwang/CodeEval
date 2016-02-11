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
            nums,switches = [l.split(' ') if i==0 else l.split(', ') for i,l in enumerate(test.split(' : '))]
            
            for switch in switches:
                n1,n2 = switch.split('-')
                nums[int(n1)], nums[int(n2)] = nums[int(n2)], nums[int(n1)]
            print ' '.join(nums)