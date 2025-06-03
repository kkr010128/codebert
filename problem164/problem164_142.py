import sys,math
input = sys.stdin.readline

A,B,C,D=list(map(int,input().split()))
if math.ceil(C/B) <= math.ceil(A/D):
    print('Yes')
else:
    print('No')