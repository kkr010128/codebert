import sys
input = sys.stdin.readline

M1,D1 = map(int, input().split())
M2,D2 = map(int, input().split())

if(M1+1==M2):print(1)
else: print(0)