#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-27 15:34:06 +0900
# LastModified: 2020-06-27 15:35:45 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a)>=h:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
