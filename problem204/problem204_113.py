#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D_fix_3
# CreatedDate:  2020-08-30 13:22:07 +0900
# LastModified: 2020-08-30 13:41:03 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    S = input()
    Q = int(input())
    appendix_1 = ''
    appendix_2 = ''
    reverse = 0
    for _ in range(Q):
        q = list(input().split())
        if q[0] == '1':
            reverse += 1
        else:
            if q[1] == '1' and reverse % 2 == 0:
                appendix_1 += q[2]
            elif q[1] == '1' and reverse % 2 == 1:
                appendix_2 += q[2]
            if q[1] == '2' and reverse % 2 == 0:
                appendix_2 += q[2]
            elif q[1] == '2' and reverse % 2 == 1:
                appendix_1 += q[2]

    if reverse % 2 == 0:
        print(appendix_1[::-1] + S + appendix_2)
    else:
        print(appendix_2[::-1] + S[::-1] + appendix_1)



if __name__ == "__main__":
    main()
