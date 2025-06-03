from itertools import combinations
n = int(input())
d = list(map(int,input().split()))
ans = 0
for x,y in combinations(range(n),2):
    ans += d[x] * d[y]
print(ans)