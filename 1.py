# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

def fb_mapper(num,x,y):
    ans = ''
    if num%x == 0:
        ans+= 'F'
    if num%y == 0:
        ans+= 'B'
    if ans == '':
        return str(num)
    return ans
    
if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path,'r') as test_cases:
        for test in test_cases:
            x,y,n = map(int,test.rstrip('\n').split(' '))
            print ' '.join([fb_mapper(i,x,y) for i in range(1,n + 1)])