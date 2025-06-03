#!/usr/bin/env python3

n = int(input())
a = []
for _ in range(n):
    a.append([[*map(int, input().split())] for _ in range(int(input()))])

ans = 0
for i in range(2**n):
    hone = set()
    unki = set()
    for j in range(n):
        if i >> j & 1:
            hone |= {j + 1}
            for k in a[j]:
                if k[1] == 1:
                    hone |= {k[0]}
                else:
                    unki |= {k[0]}
        else:
            unki |= {j + 1}
    if hone & unki == set():
        ans = max(ans, len(hone))
print(ans)
