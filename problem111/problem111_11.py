n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort(reverse=True)
for i in range(n-1):
  ii = int((i+(i%2))/2)
  ans += a[ii]
print(ans)