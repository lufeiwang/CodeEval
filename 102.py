# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys
import json

if __name__ == '__main__':
    file_path = sys.argv[1]
    
    with open(file_path,'r') as test_cases:
        for test in test_cases:
            test = test.rstrip('\n')
            menu=json.loads(test)
            ans = 0
            ans=[int(itm['id']) for itm in menu['menu']['items'] if itm != None and itm.get('label') != None]
            print str(sum(ans))