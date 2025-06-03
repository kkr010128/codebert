# -*- coding: utf-8 -*-
import sys
import numpy as np

N,S, *A = map(int, sys.stdin.buffer.read().split())
mod = 998244353

answer = np.zeros(S+1).astype(np.int64)
answer[0] = 1

for a in A:
  if a<=S:
    answer[a:] = (2*answer[a:]+answer[:-a])%mod
    answer[:a] = (2*answer[:a])%mod
  else:
    answer = (2*answer)%mod

print(answer[S])