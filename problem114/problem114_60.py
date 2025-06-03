#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-28 21:02:34 +0900
# LastModified: 2020-06-28 22:01:44 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    d = int(input())
    c = list(map(int, input().split()))
    s = []   # 満足度
    box = [-1]*26  # 各コンテストの実施日
    for i in range(d):
        s.append(list(map(int, input().split())))

    total_satisfy = 0
    for i in range(d):
        t = int(input())
        total_satisfy += s[i][t-1]
        box[t-1] = i
        for j in range(26):
            if box[j] == -1:
                total_satisfy -= c[j]*(i+1)
            else:
                total_satisfy -= c[j]*(i-box[j])
#        print(box)

        print(total_satisfy)






if __name__ == "__main__":
    main()
