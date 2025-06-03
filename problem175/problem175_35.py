import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np
from numba import njit

MOD = 10**9 + 7

N = int(readline())
S = np.array(list(read().rstrip()), np.int8)

R = np.sum(S == ord('R'))
B = np.sum(S == ord('B'))
G = np.sum(S == ord('G'))
 
@njit
def f(S):
    N = len(S)
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
          k = j + j - i
          if k >= N:
            break
          if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            ret += 1
    return ret
  
answer = R * B * G - f(S)
print(answer)