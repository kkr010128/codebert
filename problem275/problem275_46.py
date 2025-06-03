x,y=map(int,input().split())
a=[300000,200000,100000]
b=[0]*300
a=a+b
add=0
if x*y==1:
    add=400000
print(a[x-1]+a[y-1]+add)
