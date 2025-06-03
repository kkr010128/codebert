# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:19:14 2020

@author: ezwry
"""

n = int(input())
xy = [map(int, input().split()) for i in range(n)]
x, y = [list(i) for i in zip(*xy)]

"""
A,Bの場合
"""

maxab = x[0] + y[0]
minab = x[0] + y[0]

for i in range(n):
    xi = x[i]
    yi = y[i]
    mini = xi+yi
    maxi = xi+yi
    if mini < minab:
        minab = mini
    if maxi > maxab:
        maxab = maxi

maxatob = maxab - minab

"""
C,Dの場合
"""

maxcd = y[0]-x[0]
mincd = y[0]-x[0]

for j in range(n):
    maxj = y[j] - x[j]
    minj = y[j] - x[j]
    if maxj > maxcd:
        maxcd = maxj
    if minj < mincd:
        mincd = minj

maxctod = maxcd - mincd

majimax = max(maxatob, maxctod)
print(majimax)