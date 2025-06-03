# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:28:06 2018
ALDS1_5a
@author: maezawa
"""
import itertools as itr

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

sum_array = []
for r in range(1,n+1):
    for comb in itr.combinations(a, r):
        sum_array.append(sum(comb))

for i in m:
    yesorno = 'no'
    for j in sum_array:
        #print(i, j)
        if i == j:
            yesorno = 'yes'
            break
    print(yesorno)

