#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	A
# CreatedDate:  2020-06-27 15:30:40 +0900
# LastModified: 2020-06-27 15:33:43 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    h, a = map(int, input().split())
    if float(h/a).is_integer():
        print(h//a)
    else:
        print(h//a+1)


if __name__ == "__main__":
    main()
