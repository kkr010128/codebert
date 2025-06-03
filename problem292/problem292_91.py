import math
import itertools
n = int(input())
d =list(map(int,input().split()))

p = list(itertools.combinations(d, 2))
ans = 0
for i in range(len(p)):
    d = p[i][0] * p[i][1]
    ans = ans + d

print(ans)