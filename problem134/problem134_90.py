n = int(input())
A = list(map(int, input().split(' ')))

res = 1
for a in A:
    res = min(res*a, 10**18 + 1)
if res == 10**18 + 1: print(-1)
else: print(res)