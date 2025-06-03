#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)
from collections import deque

# 整数の入力
a = int(input())

print(a+a**2+a**3)