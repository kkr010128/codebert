#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D_fix
# CreatedDate:  2020-08-30 14:54:11 +0900
# LastModified: 2020-08-30 15:07:52 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    H = int(input())
    mul = 0
    while H != 1:
        mul += 1
        H //= 2
    print(2**(mul+1)-1)

if __name__ == "__main__":
    main()
