n = int(input())
v = [[tuple(map(int, input().split()))for i in range(int(input()))]
     for i in range(n)]

ans = 0
for i in range(2**n):
    f = True
    a = 0
    for j in range(n):
        if (i >> j) & 1:
            if all(i >> (x - 1) & 1 == y for x, y in v[j]):
                a += 1
            else:
                f = False
                break
    if f:
        ans = max(ans, a)
print(ans)
