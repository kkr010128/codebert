#!/usr/bin/env python
#-*- coding:utf-8 -*-

N = int(raw_input())

A = map(int,raw_input().split())
counter = 0 
for i in range(len(A)):
    for j in range(len(A) - 1, 0, -1):
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1], A[j]
            counter += 1

print ' '.join(map(str,A))
print counter