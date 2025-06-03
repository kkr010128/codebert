import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    a,b,k = LI()
    x = max(a-k,0)
    y = b
    if k-a > 0:
        y = max(b-(k-a),0)
    print(x,y)
main()