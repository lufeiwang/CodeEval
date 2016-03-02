# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path,'r') as test_cases:
        mth_d = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun':6, 'Jul':7,
             'Aug':8, 'Sep':9, 'Oct':10, 'Nov': 11, 'Dec': 12}
        list_size = 31 * 12
        
        for test in test_cases:
            periods= test.rstrip('\n').split('; ')
            l = [0 for i in range(list_size)]
            for range_i in periods:
                start_i, end_i = range_i.split('-')
                start_mth, start_year = start_i.split(' ')
                end_mth, end_year = end_i.split(' ')
                
                starting_ind = -1 + (int(start_year) - 1990) * 12 + mth_d[start_mth]
                ending_ind = (int(end_year) - 1990) * 12 + mth_d[end_mth]
                for i in range(starting_ind, ending_ind):
                    l[i] = 1
            print int(sum(l)/12)
