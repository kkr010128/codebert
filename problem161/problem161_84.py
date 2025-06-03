import sys
A,B,N = map(int, input().split())


def calc(a,b,x):
    num = ((a*x)//b)-a*(x//b)
    return num


if B == N:
    X = N-1
    print(calc(A,B,X))
    sys.exit()
if B < N:
    X = B-1
    print(calc(A,B,X))
    sys.exit()
if B > N:
    X = N
    print(calc(A,B,X))
    sys.exit()