N,K = map(int,input().split())

def solve(n,k):
  n %= k
  return min(n,abs(n-k))

print(solve(N,K))