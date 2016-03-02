# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:30:09 2016

@author: Toto
"""
import sys
import os

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        for l in f:
            n, history= l.rstrip('\n').split(';')
            history=[int(i) for i in history.split(' ')]
            running_sum=[sum(history[0:i]) for i in range(1,len(history)+1)]
            running_sum.insert(0,0)
           # print running_sum
            
            
            ans=max((running_sum[i+int(n)] - running_sum[i] for i in range(len(running_sum) - int(n))))
            print (0,ans)[ans>0]