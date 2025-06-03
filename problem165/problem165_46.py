#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-06-27 13:59:01 +0900
# LastModified: 2020-06-27 14:04:38 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = list(set(s))
    print(len(s))
        


if __name__ == "__main__":
    main()
