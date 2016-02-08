# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/92/
"""
import sys


    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            a = line.strip('\n').split(' ')
            print a[-2]
            
