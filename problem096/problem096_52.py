import math
n,d = map(int,input().split())
x = [list(map(int,input().split()))for _ in range(n)]

ans = 0

for i in range(n):
  r = math.sqrt(x[i][0]**2+x[i][1]**2)
  if r <= d:
    ans += 1

print(ans)