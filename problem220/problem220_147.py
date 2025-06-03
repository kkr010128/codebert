import sys
input = sys.stdin.readline

s,t=input().rstrip().split()
a,b=map(int,input().split())
u=input().rstrip()

if u == s:
    print(a-1,b)
else:
    print(a,b-1)
