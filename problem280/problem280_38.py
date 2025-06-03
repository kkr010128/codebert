import itertools
from math import sqrt
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cnt = 0
for v in itertools.permutations(list(range(n))):
    for i in range(n-1):
        x = (xy[v[i]][0]-xy[v[i+1]][0]) ** 2
        y = (xy[v[i]][1]-xy[v[i+1]][1]) ** 2
        ans += sqrt(x+y)
    cnt += 1
print(ans/cnt)