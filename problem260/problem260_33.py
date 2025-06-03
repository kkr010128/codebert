#!/usr/bin/env pypy3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
a1, a2, a3 = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

print('bust' if a1 + a2 + a3 >= 22 else 'win')
