from collections import Counter as coun
from itertools import combinations as comb

import sys
input = sys.stdin.readline

N = int(input())
S = input()

C = coun(S)
ans = C["R"] * C["G"] * C["B"]
for i, j in comb(range(N), 2):
  k = 2 * j - i
  if k < N:
    A, B, C = S[i], S[j], S[k]
    if A != B and B != C and C != A: ans -= 1

print(ans)
