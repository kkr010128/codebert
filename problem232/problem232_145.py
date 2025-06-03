a,b = map(int,input().split())
ans = ""
k = min(a,b)
l = max(a,b)
for i in range(l):
  ans += str(k)
print(ans)