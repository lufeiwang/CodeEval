# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""

if __name__ == '__main__':
    row_i = 1
    while row_i <= 12:
        print (''.join(['{0: >4}'.format(str((x+1)*row_i)) for x in range(12)]))
        row_i += 1
    
    