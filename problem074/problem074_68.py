n,k=list(map(int,input().split()))
s=[]
b=[0]*k
for x in range(k):
    
    l,r=list(map(int,input().split()))
    s.append((l,r))
    
d=[0]*n
d[0]=1
for i in range(1,n):
    j=0
    for l,r in s:
        if i-l>=0:
            b[j]+=d[i-l]
        if i-r-1>=0:
            b[j]-=d[i-r-1]
        
        d[i]+=b[j]
        j+=1
    d[i]%=998244353
print(d[-1])