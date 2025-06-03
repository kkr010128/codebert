import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    s = S()
    if len(s)<6:
        print('No')
        exit()
    if s[2]==s[3] and s[4]==s[5]:
        print('Yes')
    else:
        print('No')
    return

if __name__=='__main__':
    Main()