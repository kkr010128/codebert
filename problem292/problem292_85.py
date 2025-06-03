from itertools import combinations

N = int(input())
d = list(map(int, input().split()))

info = list(combinations(d, 2))

ans = 0
for x, y in info:
    ans += x*y

print(ans)
