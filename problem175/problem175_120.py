# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:23:36 2020

@author: Aruto Hosaka
"""

N = int(input())
S = input()


color = ['R','G','B']
k = 1

A = {color[0]:0,color[1]:0,color[2]:0}

for c1 in color:
    for c2 in color:
        for c3 in color:
            if c1 != c2 and c2 != c3 and c1 != c3:
                A[(c1,c2,c3)] = 0

for c1 in color:
    for c2 in color:
        if c1!=c2:
            A[(c1,c2)] = 0

for i in range(N):
    if S[i] == 'R':
        A[('G','B','R')] += A[('G','B')]
        A[('B','G','R')] += A[('B','G')]
        A[('B','R')] += A['B']
        A[('G','R')] += A['G']
    if S[i] == 'G':
        A[('R','B','G')] += A[('R','B')]
        A[('B','R','G')] += A[('B','R')]
        A[('B','G')] += A['B']
        A[('R','G')] += A['R']
    if S[i] == 'B':
        A[('G','R','B')] += A[('G','R')]
        A[('R','G','B')] += A[('R','G')]
        A[('R','B')] += A['R']
        A[('G','B')] += A['G']
    A[S[i]] += 1

counter = 0
for c1 in color:
    for c2 in color:
        for c3 in color:
            if c1 != c2 and c2 != c3 and c1 != c3:
                counter += A[(c1,c2,c3)]
                
dc = 0
for i in range(N-2):
    k = 1
    while k*2+i < N:
        if S[i+k] != S[i] and S[i] != S[i+k*2] and S[i+k] != S[i+k*2]:
            dc += 1
        k += 1
print(counter-dc)