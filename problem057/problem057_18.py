from __future__ import division, print_function
from sys import stdin
while True:
    m, f, r = (int(s) for s in stdin.readline().split())
    if m < 0 and f < 0 and r < 0:
        break
    mf = m + f
    if m < 0 or f < 0 or mf < 30:
        print('F')
    elif mf >= 80:
        print('A')
    elif mf >= 65:
        print('B')
    elif mf >= 50 or r >= 50:
        print('C')
    else:
        print('D')