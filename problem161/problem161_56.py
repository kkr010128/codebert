import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  # floor(x/b)がギリギリ割り切れない辺りが一番大きくなりそう
  # -> 実験してみるとmath.floor(a*x/b)-a*math.floor(x/b)はループしてそう
  # -> 答えはfloor(x/b)がギリギリ割り切れないときの値に決め打つぜ！
  a,b,n=LI()
  x=min(n,b-1)
  return math.floor(a*x/b)-a*math.floor(x/b)

# main()
print(main())
