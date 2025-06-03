n,k=map(int,input().split())
dp2=list(map(int,input().split()))
    
k=min(k,41)
for ki in range(1,k+1):
    ims=[0]*(n+1)
    for ni in range(n):
        if 0>ni-dp2[ni]:
            ims[0]+=1
        else:
            ims[ni-dp2[ni]]+=1
        if n<ni+dp2[ni]+1:
            ims[n]-=1
        else:
            ims[ni+dp2[ni]+1]-=1

    dp2[0]=ims[0]
    for ni in range(1,n):
        dp2[ni]=dp2[ni-1]+ims[ni]
    
for i in range(n):
    print(dp2[i],end=" ")
print()
