import sys

input = sys.stdin.readline
D,T,S = map(int,input().split())

if(D/S <= T):
    print('Yes')
else:
    print('No')