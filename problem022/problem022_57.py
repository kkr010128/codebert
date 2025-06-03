# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:23:30 2018
ALDS1-4a most simple implementation using the features of the python
@author: maezawa
"""

n = int(input())
s = map(int, input().split())
q = int(input())
t = map(int, input().split())

s_set = set(s)
t_set = set(t)
sandt = s_set & t_set
print(len(sandt))
