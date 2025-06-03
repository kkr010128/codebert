import sys
input = sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))
if len(set(L))!=n:
    print('NO')
else:
    print('YES')
