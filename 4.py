# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:11:46 2015

@author: Toto
https://www.codeeval.com/open_challenges/4/
"""
from math import sqrt

def prime_checker(x):
    for divisor in range(2,int(round(sqrt(x))) + 1):
        if x % divisor == 0:
            return False
            
    return True;
    
    
def prime_gen():
    x = 2
    while True:
        yield x
        x += 1
        while prime_checker(x) == False:
            x += 1
            
if __name__ == "__main__":
    y = prime_gen()
    print(sum([next(y) for i in range(1000)]))