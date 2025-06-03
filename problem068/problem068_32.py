# -*- coding: utf-8 -*-

import math

s = list(input())
q = int(input())

for i in range(q):
    n = list(input().split())
    if 'print' in n:
        for j in range(int(n[1]), int(n[2]) + 1):
            print(str(s[j]), end='')
        print()

    elif 'reverse' in n:
        for k in range(math.floor((int(n[2]) - int(n[1]) + 1) / 2)):
            s[int(n[1]) + k], s[int(n[2]) - k] = s[int(n[2]) - k], s[int(n[1]) + k]

    elif 'replace' in n:
        for l in range(int(n[1]), int(n[2]) + 1):
            s.pop(int(n[1]))

        count  = int(n[1])

        for m in list(n[3]):
            s.insert(count, m)
            count += 1

