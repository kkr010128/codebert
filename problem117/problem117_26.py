n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=[0 for i in range(n)]
B=[0 for i in range(m)]
A[0]=a[0]
B[0]=b[0]
for i in range(n-1):
    A[i+1]=a[i+1]+A[i]

for i in range(m-1):
    B[i+1]=b[i+1]+B[i]

ans=0
A.insert(0,0)
B.insert(0,0)

for i in range(n+1):
    x=0
    y=m
    j=(x+y)//2
    if A[i]+B[m]<=k:
        ans=max(ans,i+m)
    elif not A[i]+B[0]>k:
        
        
        while y-x>1:
            if A[i]+B[j]<=k:
                x=j
            else:
                y=j
            j=(x+y)//2
        ans=max(ans,i+x)
    
print(ans)
    
    
