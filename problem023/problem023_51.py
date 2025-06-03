#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	dic
# CreatedDate:  2020-06-30 15:07:10 +0900
# LastModified: 2020-06-30 15:09:49 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    dic = {}
    for _ in range(n):
        command, s = input().split()
        if command == 'insert':
            dic[s] = 1
#            print(dic)
        else:
            print("yes" if s in dic.keys() else "no")



if __name__ == "__main__":
    main()

