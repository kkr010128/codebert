n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
c = [0 for i in range(n+1)]
c[0] = 3
ans = 1

for i in range(n):
  ans *= c[a[i]]
  ans %= mod
  c[a[i]] -= 1
  c[a[i]+1] += 1
print (ans)
