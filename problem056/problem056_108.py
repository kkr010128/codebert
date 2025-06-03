n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in [None]*n]
b = [int(input()) for _ in [None]*m]
for a in A:print(sum(i*j for i,j in zip(a,b)))
