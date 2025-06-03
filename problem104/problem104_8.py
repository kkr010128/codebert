import sys
input = sys.stdin.readline

l,r,d=map(int,input().split())
v1 = l//d
if l%d==0:
    v1-=1
v2 = r//d
print(v2-v1)
