import math
import time
from collections import defaultdict, deque
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
s,w=map(int,stdin.readline().split())
if(w>=s):
    print("unsafe")
else:
    print("safe")
