import sys
input = sys.stdin.readline

N=int(input())
r = N%1000
if r == 0:
    print(0)
else:
    print(1000-r)