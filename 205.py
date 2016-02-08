# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:29:21 2015

@author: Toto
https://www.codeeval.com/open_challenges/205/
"""
import sys
import re

    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            a = re.split('[^a-z]+', line.strip(), flags = re.IGNORECASE)
            print (' '.join([x for x in a if x <> '']).lower())