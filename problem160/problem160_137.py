#!/usr/bin/env python3
import itertools

(n, m, q), *r = [[*map(int, t.split())] for t in open(0)]
ans = 0
for i in list(itertools.combinations_with_replacement(range(1, m + 1), n)):
    sub = 0
    for a, b, c, d in r:
        sub += d * (i[b - 1] - i[a - 1] == c)
    ans = max(ans, sub)
print(ans)
