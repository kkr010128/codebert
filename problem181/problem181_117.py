from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy


lun = [[str(i)] for i in range(10)] + [[]]
olun =[[str(i)] for i in range(10)] + [[]]

ans = [str(i) for i in range(1,10)]

while True:
    for i in range(0,10):
        lun[i] = list(map(lambda x: str(i) + x, (olun[i-1]+olun[i]+olun[i+1])))
        if i>= 1: ans += lun[i]

    if len(ans) >= 10**5 + 5: break
    olun = copy.deepcopy(lun)

k = int(input())
print(ans[k-1])

