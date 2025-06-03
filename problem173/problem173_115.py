# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:58:15 2020

@author: Aruto Hosaka
"""


N = int(input())
n15 = (N-1)//15
d15 = (N-1)%15
A = [1,2,0,4,0,0,7,8,0,0,11,0,13,14,0]
d = sum(A) - sum(A[d15+1:])
n = (n15-1)*n15//2*120+n15*60
ans = d+n
for a in A[:d15+1]:
    if a != 0:
        ans += n15*15
print(ans)