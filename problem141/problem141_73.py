n = int(input())
a = list(map(int, input().split()))
s = sum(a)
k = 1-a[0]
s -= a[0]
ans = 1

for i in range(1,n+1):
  if k*2 <= s:
    k *= 2
  else:
    k = s
  ans += k
  k -= a[i]
  s -= a[i]

if k == 0 and s == 0:
  print(ans)
else:
  print(-1)