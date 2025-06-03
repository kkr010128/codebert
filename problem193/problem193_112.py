#!/usr/bin/python3
import copy

def minOp(h, w, k, yl, s):
    xl = []
    ks = [ 0 for i in range(len(yl) + 1) ]

    for x in range(w):
        py = 0
        cks = [ 0 for i in range(len(yl) + 1) ]
        for idx, y in enumerate(yl + [h - 1]):
            for yy in range(py, y + 1):
                if s[yy][x] == '1':
                    cks[idx] += 1

            py = y + 1

        over = False
        for idx, kk in enumerate(ks):
            if kk + cks[idx] > k:
                over = True

        if over:
            for ck in cks:
                if ck > k:
                    return (h - 1) + (w - 1)
            xl.append(x - 1)
            ks = copy.copy(cks)
        else:
            ks = list(map(lambda a, b: a + b, ks, cks))
            
    return len(xl) + len(yl)
    

def devideVertical(h, w, k, cy, yl, s):
    m = (h - 1) + (w - 1)
    for y in range(cy, h - 1):
        nyl = copy.copy(yl)
        nyl.append(y)
        m = min(m, devideVertical(h, w, k, y + 1, nyl, s))
    
    m = min(m, minOp(h, w, k, yl, s))
    return m

(h, w, k) = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

print(devideVertical(h, w, k, 0, [], s))

