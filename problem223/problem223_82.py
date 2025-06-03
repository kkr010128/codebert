# -*- coding: utf-8 -*-
 
## Library
 
import sys
from fractions import gcd
import math
from math import ceil,floor
import collections
from collections import Counter
import itertools
import copy
 
## input
 
# N=int(input())
# A,B,C,D=map(int, input().split())
# S = input()
# yoko = list(map(int, input().split()))
# tate = [int(input()) for _ in range(N)]
# N, M = map(int,input().split()) 
#    P = [list(map(int,input().split())) for i in range(M)]
#    S = []
#    for _ in range(N):
#        S.append(list(input()))
 
N,K=map(int, input().split())
P = list(map(int, input().split()))

S = []

for i in range(N):
    S.append((P[i]+1)/2)

tmp = sum(S[:K])
ans = tmp

for i in range(N-K):
    tmp = tmp - S[i] + S[i+K]
    ans = max(ans, tmp)


print(ans)
