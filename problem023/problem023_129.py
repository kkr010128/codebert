# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:14:10 2018
ALDS1-4c  implementation with dictionary
@author: maezawa
"""

n = int(input())
a = dict([])
for s in range(n):
    cmd, word = input().split()
    if cmd == 'insert':
        a[word]=''
    else:
        if word in a:
            print('yes')
        else:
            print('no')


