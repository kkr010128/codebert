import sys
import copy
import math
import itertools
import numpy as np
S=input()
N = len(S)+1
a = [0]*N
b = [0]*N
for i in range(N-1):
    if S[i]=="<":
        a[i+1]=a[i]+1

for i in reversed(range(N-1)):
    if S[i]==">":
        b[i]=b[i+1]+1

for i in range(N):
    if a[i] < b[i]:
        a[i]=b[i]

print(sum(a))