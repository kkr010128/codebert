A,B,M=map(int,input().split())
a=[int(i)for i in input().split()]
b=[int(i)for i in input().split()]
xyc=[[int(i)for i in input().split()]for j in range(M)]
res=min(a)+min(b)
for x,y,c in xyc:
    tmp=a[x-1]+b[y-1]-c
    res=min(res,tmp)
print(res)