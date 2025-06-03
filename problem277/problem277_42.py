#!/usr/bin/env python3
h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = []
c = 1
for i in s:
    if i == "." * w:
        if ans:
            ans.append(ans[-1])
        else:
            ans.append([0]*w)
    else:
        f = i.index("#")
        ans.append([c] * (f + 1))
        for j in i[f + 1:]:
            if j == "#":
                c += 1
            ans[-1].append(c)
        c += 1
for i in range(h):
    if ans[i] != [0]*w:
        for j in range(i):
            ans[j] = ans[i]
        break
for i in ans:
    print(*i)
