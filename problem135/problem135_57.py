import bisect,collections,copy,heapq,itertools,math,string
import sys
from decimal import Decimal
def S(): return sys.stdin.readline().rstrip()
def M(): return map(Decimal,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, b = M()
ab = a*b
print(math.floor(ab))
