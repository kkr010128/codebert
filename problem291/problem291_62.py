import sys

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B = LI()

ans = A-B-B
if ans <= 0:
    print(0)
else:
    print(ans)