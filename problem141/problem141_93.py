from math import log2

N = int(input())
A = [int(i) for i in input().split()]

def solve() :
  m, M = A[-1], A[-1]
  max1 = [0] * (N + 1)
  max1[-1] = M
  for i in range(N - 1, -1, -1) :
    m = (m + 1) // 2 + A[i]
    M = M + A[i]
    max1[i] = M
  if not m <= 1 <= M :
    return -1
  
  ne = 1 - A[0]
  max2 = [0] * (N + 1)
  max2[0] = 1
  for i in range(1, N + 1) :
    ne = ne * 2 - A[i]
    max2[i] = ne + A[i]
    
  return sum(min(max1[i], max2[i])for i in range(N + 1))
  
print(solve())
