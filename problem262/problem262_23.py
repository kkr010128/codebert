from itertools import product

n = int(input())
l1 = []
for _ in range(n):
    l2 = []
    for _ in range(int(input())):
        l2.append(list(map(int, input().split())))
    l1.append(l2)

ans = 0
for k in product([1, 0], repeat=n):
    check = True
    for i, j in enumerate(l1):
        if k[i] == 0:
            continue
        for x in j:
            if k[x[0] - 1] != x[1]:
                check = False
    if check:
        ans = max(ans, sum(k))
print(ans)