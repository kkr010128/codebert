from itertools import combinations
N = int(input())
L = sorted(map(int, input().split()))
ans = 0
for a, b, c in combinations(L, 3):
    if a < b < c and a + b > c:
        ans += 1
print(ans)
