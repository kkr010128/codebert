# -*- coding: utf-8 -*-

import sys
import os


lst = input().split()
stack = []

for c in lst:
    if c == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)
    elif c == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif c == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
    else:
        stack.append(int(c))
print(stack[0])