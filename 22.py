# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/22/
"""
import sys
import re

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = int(line.rstrip('\n'))
            print fib(line)
            