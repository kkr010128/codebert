import math
import collections
K = int(input())
S = input()
L = list(S)
if len(L) <= K:
  print(S)
else:
  M = L[:K]
  print(''.join(M)+'...')
