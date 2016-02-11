# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    
    with open(file_path,'r') as test_cases:
        for test in test_cases:
            test = test.rstrip('\n')
            [scrambled_sentence, seq] = test.split(';')
            words = scrambled_sentence.split(' ')
            order_seq = seq.split(' ')
            
            last_word = words[-1] #store last word 
            d = {}
            
            for i,val in enumerate(order_seq):
                d[int(val)]=words[i]
            
            ans=[]
            for i in range(len(words)):
                if d.get(int(i) + 1) == None:
                    ans.append(last_word)
                else:
                    ans.append(d[int(i) + 1])
            print ' '.join(ans)