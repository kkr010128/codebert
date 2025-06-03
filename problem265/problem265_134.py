# -*- coding:utf-8 -*-
import math

n = int(input())
ret_just = math.floor(n/1.08)
ret_minus1 = ret_just - 1
ret_plus1 = ret_just + 1

if math.floor(ret_just*1.08) == n:
    print(ret_just)
elif math.floor(ret_minus1*1.08) == n:
    print(ret_minus1)
elif math.floor(ret_plus1*1.08) == n:
    print(ret_plus1)
else:
    print(":(")
