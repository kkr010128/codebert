# -*- coding: utf-8 -*-

import sys
import os

#input_text_path = __file__.replace('.py', '.txt')
#fd = os.open(input_text_path, os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

a, b = list(map(int, input().split()))
if a > b:
    print('a > b')
elif a == b:
    print('a == b')
else:
    print('a < b')