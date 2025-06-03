import sys
n,k=map(int,input().split())
A=[]
mod=10**9+7

zero=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]>0:
        A.append([a[i],0])
    elif a[i]<0:
        A.append([-a[i],1])
    else:
        zero+=1        
if k>n-zero:
    print(0)
    sys.exit()

A=list(reversed(sorted(A)))
cnt=0
for i in range(k):
    cnt+=A[i][1]
chk=0
for i in range(n-zero):
    chk+=A[i][1]    

if cnt%2==0:
    ans=1
    for i in range(k):
        ans=ans*A[i][0]%mod
    print(ans)
elif chk==n-zero:
    if zero>0:
        print(0)
        sys.exit()
    ans=1
    for i in range(k):
        ans=ans*A[n-i-1][0]%mod
    print((-ans)%mod)
elif k==n-zero:
    ans=1
    if zero>0:
        print(0)
    else:
        for i in range(k):
            ans=ans*A[i][0]%mod
        print((-ans)%mod)
        
else:
    if A[k][1]==0:
        p=A[k][0]
        m=0
        for i in range(k+1,n-zero):
            if A[i][1]==1:
                m=A[i][0]
                break
    else:
        m=A[k][0]
        p=0
        for i in range(k+1,n-zero):
            if A[i][1]==0:
                p=A[i][0]
                break
    #print(m,p)
    if A[k-1][1]==0:
        l=0
        Xl=-1
        for i in range(k-1):
            if A[k-i-2][1]==1:
                l=A[k-i-2][0]
                Xl=k-i-2
                break
        #print(l,k)
        if m*l>p*A[k-1][0] or Xl==-1:
            ans=1
            for i in range(k-1):
                ans=ans*A[i][0]%mod
            ans=ans*m%mod
            print(ans)
        else:
            ans=1
            for i in range(k):
                if i==Xl:
                    continue
                ans=ans*A[i][0]%mod 
            ans=ans*p%mod
            print(ans)
    else:
        l=0
        Xl=-1
        for i in range(k-1):
            if A[k-i-2][1]==0:
                l=A[k-i-2][0]
                Xl=k-i-2
                break
        #print(l,k)
        if p*l>m*A[k-1][0] or Xl==-1:
            ans=1
            for i in range(k-1):
                ans=ans*A[i][0]%mod
            ans=ans*p%mod
            print(ans)
        else:
            ans=1
            for i in range(k):
                if i==Xl:
                    continue
                ans=ans*A[i][0]%mod 
            ans=ans*m%mod
            print(ans)