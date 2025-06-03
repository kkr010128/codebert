import heapq
import sys
input = sys.stdin.readline
n = int(input())
s = [input() for _ in range(n)]
t = []
p = []
for i in range(n):
    k = 0
    m = 0
    for c in s[i]:
        if c == '(':
            k += 1
        elif c == ')':
            k -= 1
            m = min(k, m)
    if k >= 0:
        t.append((-m, k))
    else:
        k = 0
        m = 0
        for c in s[i][::-1]:
            if c == ')':
                k += 1
            elif c == '(':
                k -= 1
                m = min(k, m)
        p.append((-m, k))
t.sort()
p.sort()
hq = []
hq1 = []
d = 0
idx = 0
for i in range(len(t)):
    while idx < len(t) and d >= t[idx][0]:
        m, k = t[idx]
        heapq.heappush(hq, (-k, m))
        idx += 1
    if hq:
        k, m = heapq.heappop(hq)
    else:
        print('No')
        break
    d -= k
else:
    d1 = 0
    idx = 0
    for i in range(len(p)):
        while idx < len(p) and d1 >= p[idx][0]:
            m, k = p[idx]
            heapq.heappush(hq1, (-k, m))
            idx += 1
            if hq1:
                k, m = heapq.heappop(hq1)
            else:
                print('No')
                break
            d1 -= k
    else:
        if d == d1:
            print('Yes')
        else:
            print('No')
