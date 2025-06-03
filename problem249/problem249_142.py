import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, K = map(int, input().split())

ansA = A
ansB = B
ansA -= min(A, K)
K -= A - ansA
ansB -= min(B, K)
print(ansA, ansB)