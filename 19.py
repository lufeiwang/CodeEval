# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/19/
"""
import sys


    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            a = line.rstrip('\n').split(',')
            index_a = int(a[1])
            index_b = int(a[2])
            num = bin(int(a[0]))
            if num[-1 * index_a] == num[-1 * index_b]:
                print 'true'
            else:
                print 'false'
            
            
