# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/156/
"""
import sys

def roller_generator():
    while True:
        yield True
        yield False
         
def process_rollertext(line):
    y = roller_generator()
    res = ''
    for i,x in enumerate(line):
        if x.isalpha():
            if next(y) == True: #caps
                res += x.upper()
            else:
                res += x.lower()
        else:
            res += x
    return res
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            print process_rollertext(line)