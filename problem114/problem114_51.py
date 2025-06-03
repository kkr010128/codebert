# -*- coding: utf-8 -*-

D = int(input())
c = list(map(int, input().split()))
s = []
t = []

for i in range(D):
    s.append(list(map(int, input().split())))

for i in range(D):
    t.append(int(input()) - 1)

last = [0] * 26

ans = 0

for i in range(D):
    ans = ans + s[i][t[i]]
    for j in range(26):
        if t[i] != j:
            last[j] += 1
            ans = ans - (c[j] * last[j])
        elif t[i] == j:
            last[j] = 0
    print(ans)