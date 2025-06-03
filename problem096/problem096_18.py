import sys

N, D = map(int,input().split())
X = [0]*N
Y = [0]*N
for i in range(N):
  X[i], Y[i] = map(int,input().split())

def solve():
  ret = 0
  for i in range(N):
    if X[i]*X[i]+Y[i]*Y[i] <= D*D:
      ret += 1
  return ret

print(solve())