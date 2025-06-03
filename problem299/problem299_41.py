import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    la = [(item,i+1) for i,item in enumerate(a)]
    la.sort()
    for rep in la:
        print(f"{rep[1]} ",end="")
    return

if __name__=='__main__':
    n = I()
    a = list(IL())
    solve()