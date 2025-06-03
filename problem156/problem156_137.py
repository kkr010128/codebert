from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

x = int(stdin.readline().rstrip())

for i in range(-150,150):
    for j in range(-150,150):
        if i**5-j**5 == x: print(i,j); sys.exit()
