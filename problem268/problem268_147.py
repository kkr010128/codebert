from collections import defaultdict

N=int(input())
*A,=map(int,input().split())
mod = 10**9+7

count = defaultdict(int)
count[0] = 3

ans = 1
for i in range(N):
  ans *= count[A[i]]
  ans %= mod
  count[A[i]] -= 1
  count[A[i]+1] += 1
  
print(ans)