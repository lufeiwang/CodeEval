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
            seq = test.split(' ')
            
            ans = ''
            for i in range(1,len(seq),2):
                if seq[i-1] == '0':
                    ans += ('{0:0<' + str(len(seq[i]))+'}').format('')
                else:
                    ans += ('{0:1<' + str(len(seq[i]))+'}').format('')
            print str(int(ans,2))