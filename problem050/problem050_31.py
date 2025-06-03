# -*- coding: utf-8 -*-

import sys
import os


def frame(w, h):
    top = '#' * w

    inner = ['.'] * w
    inner[0] = '#'
    inner[-1] = '#'
    inner_str = ''.join(inner)

    print(top)
    for i in range(h - 2):
        print(inner_str)
    print(top)


for s in sys.stdin:
    H, W = list(map(int, s.split()))
    if W == H == 0:
        break
    else:
        frame(W, H)
        print()