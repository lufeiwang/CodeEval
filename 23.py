# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""

if __name__ == '__main__':
    row_i = 1
    while row_i <= 12:
        print (''.join([str((x+1)*row_i).rjust(4,' ') for x in range(12)]))
        row_i += 1
    
    