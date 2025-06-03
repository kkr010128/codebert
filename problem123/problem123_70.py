import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))
xa=a[0]
for i in range(1,len(a)):
    xa ^= a[i]
b = []
for ai in a:
    b.append(xa^ai)
print(*b)
