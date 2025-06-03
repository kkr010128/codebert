def sell(m,s,a):
  return m+s*a,0

def buy(m,a):
  return m%a,m//a

def solve():
  m = 1000
  s = 0
  N = int(input())
  A = list(map(int, input().split()))
  for i in range(N-1):
    m,s = sell(m,s,A[i])
    if A[i]<A[i+1]:
      m,s = buy(m,A[i])
  m,s = sell(m,s,A[-1])
  return m
print(solve())