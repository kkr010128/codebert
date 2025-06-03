import numpy as np
from numba import njit

N,K = map(int, input().split())
A = np.array(list(map(int, input().split())))

@njit
def main(N, K, A):
  for _ in range(min(K, 42)):
    A_ = np.zeros_like(A)
    for n in range(N):
      A_[max(0, n - A[n])] += 1
      if n + A[n] + 1  < N:
        A_[n + A[n] + 1] -= 1
    A = A_.cumsum()
        
  return A

print(*main(N, K, A))