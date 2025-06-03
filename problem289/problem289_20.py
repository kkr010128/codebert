import sys
from collections import deque
from decimal import Decimal
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    a,b,x = IL()
    v = a*a*b
    if v/2<=x:
        ang = math.atan((v-x)*2/a**3)
    else:
        ang = math.atan(a*b*b/2/x)
    print(math.degrees(ang))
    return

if __name__=='__main__':
    Main()