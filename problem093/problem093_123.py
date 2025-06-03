#!/usr/bin python3
# -*- coding: utf-8 -*-

n, k = map(int, input().split())
p = [int(i)-1 for i in input().split()]
c = list(map(int, input().split()))

rc = [0] * n
rp = [0] * n
for i in range(n):
    if rc[i]!=0:
        continue
    else:
        nw = set([i])
        np = c[i]
        nx = p[i]
        while not nx in nw:
            nw.add(nx)
            np += c[nx]
            nx = p[nx]
        cnt = len(nw)
        for x in nw:
            rc[x] = cnt
            rp[x] = np
ret = - 10 ** 18
for i in range(n):
    if rc[i] == 1:
        if rp[i]>=0:
            ret = max(ret, k*rp[i])
        else:
            ret = max(ret, rp[i])
        continue
    pseq = [0]
    nx = p[i]
    for j in range(1,rc[i]+1):
        pseq.append(pseq[-1]+c[nx])
        nx = p[nx]
    pseq = pseq[1:]
    if k <= rc[i]:
        ret = max(ret, max(pseq[:k]))
    elif rp[i] < 0:
        ret = max(ret, max(pseq))
    else:
        tmp = max(pseq)
        if k%rc[i]!=0:
            tmp = max(tmp, rp[i] + max(pseq[:k%rc[i]]))
        tmp += rp[i]*(k//rc[i]-1)
        ret = max(ret, tmp)
print(ret)
