# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:35:25 2016

@author: Toto
"""
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    l=[(-1, 'This program is for humans'),
       (2,"Still in Mama's arms"),
       (4,"Preschool Maniac"),
       (11,"Elementary school"),
       (14,'Middle school'),
       (18,'High school'),
       (22, 'College'),
       (65,'Working for the man'),
       (100, 'The Golden Years')]

    with open(file_path,'r') as test_cases:
        for test in test_cases:
            age = int(test.rstrip('\n'))
            ans = 'This program is for humans'
            for i in l:
                if age <= i[0]:
                    ans = i[1]
                    break
            print ans
       