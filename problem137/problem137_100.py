
n=int(input())
a=[]
b=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)

a.sort()
b.sort()
    
if n%2==0:
    n2=n//2
    ca=(a[n2-1]+a[n2])
    cb=(b[n2-1]+b[n2])
    c=cb-ca+1
else:
    n2=(n-1)//2
    ca=a[n2]
    cb=b[n2]
    c=cb-ca+1
    
print(c)
