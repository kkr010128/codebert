import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

a, b, c = mapint()

if c-(a+b)>=0:
    if 4*a*b<(c-a-b)**2:
        print('Yes')
    else:
        print('No')
else:
    print('No')