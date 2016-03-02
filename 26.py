# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:30:09 2016

@author: Toto
"""
import sys
import os

if __name__=='__main__':
    print os.stat(sys.argv[1]).st_size