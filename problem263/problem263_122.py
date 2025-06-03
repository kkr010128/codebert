import sys
readline = sys.stdin.readline
import numpy as np

N = int(readline())
A = np.array(readline().split(),dtype=int)
DIV = 10 ** 9 + 7

# 各桁の1と0の数を数えて、((1の数) * (0の数)) * (2 ** i桁目(1桁目を0とする))を数える

K = max(A)
  
j = 0
ans = 0
while K:
  bits = (A >> j) & 1
  one = np.count_nonzero(bits)
  ans += (one % DIV) * ((N - one) % DIV) * pow(2,j,DIV)
  ans %= DIV
  j += 1
  K >>= 1

print(ans)