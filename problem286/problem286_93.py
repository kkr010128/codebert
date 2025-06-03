import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()
if 1<=A<=9 and 1<=B<=9:
    print(A*B)
else:
    print(-1)