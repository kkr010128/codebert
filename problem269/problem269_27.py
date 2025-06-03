import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

T1, T2 = mapint()
A1, A2 = mapint()
B1, B2 = mapint()

if not (A1-B1)*(A2-B2)<0:
    print(0)
else:
    if A1<B1:
        A1, B1 = B1, A1
        A2, B2 = B2, A2
    if A1*T1+A2*T2==B1*T1+B2*T2:
        print('infinity')
        exit(0)
    rest = (A1-B1)*T1
    come = (B2-A2)*T2
    if come<rest:
        print(0)
    else:
        ans = come//(come-rest)
        last = 1 if come%(come-rest)==0 else 0
        print(ans*2-1-last)