from math import ceil
from bisect import bisect_right

n, d, a = map(int, input().split())
l = []
l2 = []
l3 = []
l4 = [0 for i in range(n+1)]
l5 = [0 for i in range(n+1)]
ans = 0
for i in range(n):
  x, h = map(int, input().split())
  l.append([x, h])
  l2.append(x + 2 * d)
  l3.append(x)
l.sort(key=lambda x: x[0])
l2.sort()
l3.sort()
for i in range(n):
  cnt = ceil((l[i][1] - l4[i] * a) / a)
  if cnt > 0:
    ans += cnt
    ind = bisect_right(l3, l2[i])
    l5[ind] += cnt
    l4[i] += cnt
  l4[i+1] = l4[i] - l5[i+1]
    
print(ans)