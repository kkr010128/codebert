n,p=map(int,input().split())
s=input()
ans=0
if p==2:
    for i in range(n):
        if int(s[i])%2==0:
            ans+=i+1
    print(ans)
elif p==5:
    for i in range(n):
        if int(s[i])%5==0:
            ans+=i+1
    print(ans)
else:
    s=s[::-1]
    accum=[0]*n
    d=dict()
    for i in range(n):
        accum[i]=int(s[i])*pow(10,i,p)%p
    for i in range(n-1):
        accum[i+1]+=accum[i]
        accum[i+1]%=p
    accum[-1]%=p
    #print(accum)
    for i in range(n):
        if accum[i] not in d:
            if accum[i]==0:
                ans+=1
            d[accum[i]]=1
        else:
            if accum[i]==0:
              ans+=1
            ans+=d[accum[i]]
            d[accum[i]]+=1
    #print(d)
    print(ans)