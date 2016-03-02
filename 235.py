# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path,'r') as test_cases:
        card_raw={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                  '9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
        for test in test_cases:
            cards, trump= test.rstrip('\n').split(' | ')
            card_values = []
            cards = cards.split(' ')
            
            for card in cards:
                if trump in card:
                    card_values.append((card,13 + card_raw[card[0:-1]] - 1))
                else:
                    card_values.append((card,card_raw[card[0:-1]] - 1))
            max_val= max(card_values,key=lambda (x,y): y)[1]
            print ' '.join([x for (x,y) in card_values if y == max_val])
