from itertools import combinations

N = int(input())
takoyaki = list(int(x) for x in input().split())

life = 0

for c in combinations(range(N), 2):
    life += takoyaki[c[0]] * takoyaki[c[1]]

print(life)
