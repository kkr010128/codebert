from numpy import cumsum
n,k=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
p=cumsum(p)
print((p[k-1]))