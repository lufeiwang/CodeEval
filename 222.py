# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/222/
"""
import sys

def black_pot_winner (names, lucky_num):
    cur_num = 0 
    while len(names) > 1:
        if (lucky_num - cur_num) % len(names)== 0: # remove last person
            names = names[:-1]
        else:
            del names[(lucky_num - cur_num) % len(names) - 1]
    return names[0]
    
def parser_black_pot(line):
    return line.split(' | ')[0].split(' '),int(line.split(' | ')[1])        
            
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            [names, lucky_num] = parser_black_pot(line)
            print black_pot_winner(names, lucky_num)