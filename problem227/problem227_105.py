#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-27 15:37:37 +0900
# LastModified: 2020-06-27 15:43:18 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    if n<=k:
        print(0)
        return
    h.sort()
#    print(h)
    print(sum(h[:n-k]))



if __name__ == "__main__":
    main()
