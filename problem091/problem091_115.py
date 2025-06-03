from itertools import combinations

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0

for a,b,c in combinations(L, 3):
    ans += a < b < c < a+b

print(ans)