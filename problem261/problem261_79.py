import numpy as np
import scipy as sp
import math

S = input()
n = len(S)
m = n//2
l = 0
for i in range (0,m):
  if(S[i] != S[n-i-1]):
      l = l + 1
print(l)