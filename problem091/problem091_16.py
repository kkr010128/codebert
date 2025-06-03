from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

ans = 0

for a, b, c in combinations(L, 3):
    if a == b or b ==c or a == c:
        continue
    if a + b + c - max(a, b, c) > max(a, b, c):
        ans += 1

print(ans)