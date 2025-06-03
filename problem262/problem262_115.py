from itertools import product

n = int(input())

memo = [[] for _ in range(n)]

for i in range(n):
    for _ in range(int(input())):
        x, y = map(int, input().split())
        memo[i].append((x-1, y))

ans = 0
for a in product([0,1], repeat=n):
    REAL = True
    for i in range(n):
        if a[i] == 1:
            for x, y in memo[i]:
                if a[x] != y:
                    REAL = False
                    break
        if REAL == False:
            break

    if REAL:
        ans = max(ans, sum(a))

print(ans)