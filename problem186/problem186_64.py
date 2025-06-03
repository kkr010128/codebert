# -*- coding: utf-8 -*-
k, n = map(int, input().split())
a = list(map(int, input().split()))
fst = a[0]
a.append(k+fst)
dis= []
for i in range(n):
    dis.append(a[i+1]-a[i])
print(sum(dis)-max(dis))