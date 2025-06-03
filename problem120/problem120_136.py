# -*- coding: utf-8 -*-
n, k = map(int,input().split())
p = [int(i) for i in input().split()]

p.sort()
print(sum(p[:k]))
