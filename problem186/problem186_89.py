k,n = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
m = a[0] + k - a[n-1]
for i in range(n-1):
  l = a[i+1] - a[i]
  if l > m:
    m = l
ans = k - m
print(ans)