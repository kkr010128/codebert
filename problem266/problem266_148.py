#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
x  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

n = x // 100
mod = x % 100
print(0 if 5 * n < mod else 1)

