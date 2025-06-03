import math as mt
import sys, string
from collections import Counter, defaultdict
input = sys.stdin.readline

# input functions
I = lambda : int(input())
M = lambda : map(int, input().split())
ARR = lambda: list(map(int, input().split()))

n = I()
print(int(not n))