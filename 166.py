# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:30:09 2016

@author: Toto
"""
import sys

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        for l in f:
            t1,t2=l.rstrip('\n').split(' ')
            h1,m1,s1=[int(i) for i in t1.split(':')]
            h2,m2,s2=[int(i) for i in t2.split(':')]

            num_diff=abs((h1-h2)*3600 + (m1-m2) * 60 + s1-s2)
            print '{0:0>2}'.format(num_diff/3600) + ':' + '{0:0>2}'.format((num_diff%3600)/60) + ':' + '{0:0>2}'.format((num_diff%3600)%60) 