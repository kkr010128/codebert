# -*- coding: utf-8 -*-

n = int(raw_input())
tp = hp = 0
for i in range(n):
    ts, hs = map(str, raw_input().split())
    if ts > hs:
        tp += 3
    elif ts < hs:
        hp += 3
    else:
        tp += 1
        hp += 1
print "%d %d" %(tp, hp)