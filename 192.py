# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:30:09 2016

@author: Toto
"""
import sys

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        for l in f:
            l = l.rstrip('\n')
            o,p,q,r=[int(i) for i in l.split(' ')]
            
            ans = ''
            if r > p: # north
                ans+='N'
            elif r < p: #south
                ans+='S'
            if q>o: #east
                ans+='E'
            elif q<o: #west
                ans+='W'
            if ans=='':
                ans+='here'
            print ans