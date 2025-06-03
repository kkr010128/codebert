import numpy as np
 
N, M = map(int, input().split())
A = []
A = map(int, input().split())
 
dif = N - sum(A)
 
if dif >= 0:
  print(dif)
else:
  print('-1')