n=int(input())
a=list(map(int,input().split()))
m=max(a)
b=[0]
b*=m
for i in range(n):
    b[a[i]-1]+=1
c=[]
for i in range(m):
    if b[i]>=2:
        c.append(int(b[i]*(b[i]-1)/2))
    else:
        c.append(0)
d=sum(c)
for i in range(n):
    if c[a[i]-1]>=1:
        e=c[a[i]-1]-int((b[a[i]-1]-1)*(b[a[i]-1]-2)/2)
        print(d-e)
    else:
        print(d)

