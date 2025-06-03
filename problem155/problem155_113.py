#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix_2
# CreatedDate:  2020-08-08 01:59:29 +0900
# LastModified: 2020-08-08 02:11:36 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m  = map(int, input().split())
    h = [0] + list(map(int, input().split()))
    path = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        path[a].append(h[b])
        path[b].append(h[a])
    ans = 0
    for index in range(1, n+1):
        if path[index] and h[index] > max(path[index]):
            ans += 1
        elif not path[index]:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
