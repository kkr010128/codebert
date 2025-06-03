from collections import defaultdict
from itertools import accumulate
import bisect


n,k = map(int, input().split())

a = list(map(int,input().split()))

s = list(accumulate([0]+a))

b = [s[i]-i for i in range(n+1)]

d = defaultdict(list)

for i in range(n+1):
    d[b[i]%k].append(i)

ans = 0
for x in d.keys():
    l = d[x]
    for j in range(len(l)):
        y = l[j]
        ans += max(0,bisect.bisect_right(l,k+y-1)-j-1)

print(ans)


