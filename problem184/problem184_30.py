# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:57:22 2020
"""

import sys
#import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9+7

S = input()

if S[2] == S[3] and S[4] == S[5]:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
