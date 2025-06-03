n = int(input())
a = list(map(int,input().split()))
ans = 0
m = a[0]
for i in range(1,n):
  if a[i] <= m:
    ans += -a[i]+m
  else:
    m = a[i]
print(ans)
