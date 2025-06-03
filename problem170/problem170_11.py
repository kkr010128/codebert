from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
from functools import reduce

n,k = list(map(int, input().split()))

a = n*(n+k+1)*(n-k+2)//2
b = n-k+2
c = -((n+2)*(n+1)*n - k*(k-1)*(k-2))//3

print((a+b+c) % (10**9+7))