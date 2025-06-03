from itertools import combinations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i, j in combinations(xy, 2):
    ans += ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
print(ans * 2 / n)