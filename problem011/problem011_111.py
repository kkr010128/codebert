# -*- coding: utf-8 -*-

import sys
import os
import math


a, b = list(map(int, input().split()))
# a?????§?????????????????????
if b > a:
    a, b = b, a

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(a, b)
print(result)