# coding: utf-8
# Your code here!
import numpy as np
import sys
N,A,B=map(int,input().split())

count=int(N/(A+B))
s=N%(A+B)

if s<=A:
    print(A*count+s)
else:
    print(A*count+A)