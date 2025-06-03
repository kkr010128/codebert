# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break
    l = [int(x) for x in list(str(n))]
    print(sum(l))

