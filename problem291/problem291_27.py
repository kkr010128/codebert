import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a,b=mi()
print(max(a-b-b,0))