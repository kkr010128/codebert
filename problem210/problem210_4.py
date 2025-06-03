#!/usr/bin/python3
import bisect

n = int(input())
s = input()
q = int(input())

idxs = [ [] for i in range(26) ]
sl = [ s[i] for i in range(n) ]

for i in range(n):
    idxs[ord(s[i]) - ord('a')].append(i + 1)

#print(idxs)

qs = []
for i in range(q):
    qs.append(input())

for qi in qs:
    (op, x, y) = qi.split()
    if op == '1':
        j = int(x)
        c = y
        oc = sl[j - 1]
        if oc != c:
            sl[j - 1] = c
            idx = bisect.bisect_left(idxs[ord(oc) - ord('a')], j)
            del idxs[ord(oc) - ord('a')][idx]
            idx = bisect.bisect_left(idxs[ord(c) - ord('a')], j)
            idxs[ord(c) - ord('a')].insert(idx, j)
        
    elif op == '2':
        l = int(x)
        r = int(y)
        c = 0
        for i in range(26):
            il = bisect.bisect_left(idxs[i], l)
            ir = bisect.bisect_right(idxs[i], r)
            if il < ir:
                c += 1
        print(c)
