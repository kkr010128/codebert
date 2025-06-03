import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, b, k = M()
if k >= a:
    k -= a
    a = 0
else:
    a -= k
    k = 0
if k >= b:
    b = 0
else:
    b -= k
print(a, b)