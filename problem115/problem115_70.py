import sys
import math
import collections
import heapq
import queue
import itertools
import functools
import operator
import time

readline = sys.stdin.readline
 
IPS = lambda: readline().rstrip()
IP = lambda: int(readline().rstrip())
MP = lambda: map(int, readline().split())
LS = lambda: list(map(int, readline().split()))

def solve():
    for _ in range(1):
        n = IP()
        print(n + n**2 + n**3)
       
       
if __name__ == "__main__":
    solve()