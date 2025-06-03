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

N = int(input())

c = [[0 for i in range(10)] for _ in range(10)]
def f(n):
    x = 0
    while n > 0:
        n //= 10
        x +=1
    return x

for i in range(1, N + 1):
    d = f(i)
    front = i // (10 ** (d - 1)) 
    back = i % 10
    c[front][back] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += c[i][j] * c[j][i]
print(ans)
