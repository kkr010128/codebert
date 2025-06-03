"""
author : halo2halo
date : 9, Jan, 2020
"""

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(readline())
print(int(N**2))
