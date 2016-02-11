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
            d = {}
            test = test.rstrip('\n')
            countries = test.split(' | ')
            for i,country in enumerate(countries):
                teams = country.split(' ')
                for team in teams:
                    if d.get(int(team)) == None:
                        d[int(team)]=[str(i+1)]
                    else:
                        d[int(team)].append(str(i+1))
            
            keys_sorted=sorted(d.keys())
            ans=['' + str(k) + ':' + ','.join(d[k]) + ';' for k in keys_sorted]
            print ' '.join(ans)
