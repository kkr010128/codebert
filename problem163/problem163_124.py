import itertools
import math

s, w = map(int, input().split())
if s <= w:
    print("unsafe")
else:
    print("safe")