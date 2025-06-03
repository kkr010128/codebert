n, k = map(int, input().split())
a = list(map(int, input().split()))
a[0] = (a[0]-1)%k
for i in range(1,n):
  a[i] = (a[i]+a[i-1]-1)%k
ans = 0
b = {0:1}
for i in range(n):
  if i>0:
    b[a[i-1]] = b.get(a[i-1],0) + 1
  if i>=k:
    b[a[i-k]] -= 1
  if i==k-1:
    b[0] -= 1
  ans += b.get(a[i],0)
print(ans)