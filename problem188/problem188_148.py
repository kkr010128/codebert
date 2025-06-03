from collections import *
x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
p.sort(reverse=True)
q=list(map(int,input().split()))
q.sort(reverse=True)
r=list(map(int,input().split()))
r.sort(reverse=True)
r=r+p[:x]+q[:y]
r.sort(reverse=True)
r=r[:x+y]
print(sum(r))
