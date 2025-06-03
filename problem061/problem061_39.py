# -*- coding: utf-8 -*-
import sys
def func2(x):
    if not x.isalpha():
        return x
    else:
        if x.isupper():
            return x.lower()
        else:
            return x.upper()
print("".join(map(lambda x:func2(x),sys.stdin.readline().rstrip())))
