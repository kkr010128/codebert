n = int(input())
h = [[] for _ in range(n)]
u = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        if y == 1:
            h[i].append(x)
        elif y == 0:
            u[i].append(x)

ans = 0
for i in range(2**n):
    hs, us = set(), set()
    honest, unkind = set(), set()
    for j in range(n):
        if i & (1 << j):
            hs |= set(h[j])
            us |= set(u[j])
            honest.add(j+1)
        else:
            unkind.add(j+1)
    if not hs <= honest:
        continue
    if not us <= unkind:
        continue
    ans = max(ans, len(honest))

print(ans)