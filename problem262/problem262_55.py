from itertools import product
n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    c = int(input())
    for j in range(c):
        x, y = map(int, input().split())
        x-=1
        a[i].append([x, y])

ans = 0
for c in product([1, 0], repeat=n):
    f = True
    for i, p in enumerate(c):
        if p == 1:
            for x, y in a[i]:
                if c[x] != y:
                    f = False
                    break
        if not f:
            break
    if f:
        ans = max(ans, sum(c))
print(ans)
