N = int(input())
a = list(map(int, input().split()))

ans = 0
h = a[0]
for i in range(1,N,1):
  if h < a[i]:
    h = a[i]
  else:
    ans += (h - a[i])
print(ans)