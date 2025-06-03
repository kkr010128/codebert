n,x,y = map(int,input().split())
ans = [0] * (n-1)
l = list(range(1,n+1))

import itertools

for a,b in itertools.combinations(l, 2):
    dis = min(b-a, abs(b-y)+abs(x-a)+1)
    ans[dis-1] += 1

for i in ans:
    print(i)