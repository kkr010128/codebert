from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

ans = 0
di = defaultdict(int)
for i, a in enumerate(A):
    ans += di[i+1 - a]
    di[i+1 + a] += 1

print(ans)