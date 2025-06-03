#!/usr/bin/env python

H, W, M = map(int, input().split())
h = [-1 for _ in range(M)]
w = [-1 for _ in range(M)]
s = set()
for i in range(M):
    h[i], w[i] = map(int, input().split())
    h[i] -= 1
    w[i] -= 1
    s.add((h[i], w[i]))

# calc
hs = [0 for _ in range(H)]
ws = [0 for _ in range(W)]
for i in range(M):
    hs[h[i]] += 1
    ws[w[i]] += 1

#print('hs =', hs)
#print('ws =', ws)

hmax = max(hs)
wmax = max(ws)

ks = []
js = []

# 最大値の荷物がある場所を覚えておく
for k in range(H):
    if hmax == hs[k]:
        ks.append(k)
for j in range(W):
    if wmax == ws[j]:
        js.append(j)

ans = hmax + wmax

# クロスする場所に荷物があるかないかの確認
for k in range(len(ks)):
    for j in range(len(js)):
        if (ks[k], js[j]) not in s:
            print(ans)
            exit()
print(ans-1)