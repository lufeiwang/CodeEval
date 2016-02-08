# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/18/
"""
import sys


    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            a = line.rstrip('\n').split(',')
            x = int(a[0])
            n = int(a[1])
                        
            bin_x = bin(x)
            bin_n = bin(n)
            
            start_try = pow(2,len(bin_x) - len(bin_n))
            while start_try * n < x:
                start_try += 1
            print start_try * n
            
            
