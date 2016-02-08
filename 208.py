# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/208/
"""
import sys

def interpret_input(line):
    res=[]
    for col in range(len(line.split(' | ')[0].split(' '))):
        res.append([int(line.split(' | ')[row].split(' ')[col]) for row in range(len(line.split(' | ')))])
    
    answer = '';
    for col in res:
        answer += ' ' + str(max(col))
    return answer
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            print(interpret_input(line))
            