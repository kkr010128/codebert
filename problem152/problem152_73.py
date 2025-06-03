#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
increasing = []
decreasing = []
dec_special = []
for _ in range(n):
    s = input().rstrip()
    minima = 0
    fin = 0
    for ch in s:
        if ch == ")":
            fin -= 1
            if fin < minima:
                minima = fin
        else:
            fin += 1
    if fin >= 0:
        increasing.append((minima, fin))
    elif minima < fin:
        dec_special.append((minima, fin))
    else:
        decreasing.append((minima, fin))

increasing.sort(reverse=True)
decreasing.sort()
dec_special.sort()

current = 0
for minima, diff in increasing:
    if current + minima < 0:
        print("No")
        exit()
    current += diff
for minima, diff in dec_special:
    if current + minima < 0:
        print("No")
        exit()
    current += diff
for minima, diff in decreasing:
    if current + minima < 0:
        print("No")
        exit()
    current += diff
if current != 0:
    print("No")
else:
    print("Yes")
