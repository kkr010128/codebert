import math
n=int(input())
xs=list(map(float,input().split()))
ys=list(map(float,input().split()))
ds=[ abs(x - y) for (x,y) in zip(xs,ys) ]
print('{0:.6f}'.format(sum(ds)))
print('{0:.6f}'.format((sum(map(lambda x: x*x,ds)))**0.5))
print('{0:.6f}'.format((sum(map(lambda x: x*x*x,ds)))**(1./3.)))
print('{0:.6f}'.format(max(ds)))