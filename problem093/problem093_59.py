n,k=map(int,input().split())
*p,=map(int,input().split())
*c,=map(int,input().split())

ans=-10**20
for i in range(n):
    loop=1
    j=p[i]-1
    acm=[c[j]]
    while j!=i:
        j=p[j]-1
        acm.append(acm[-1]+c[j])
        loop+=1
    
    if acm[-1]>0:
        if k<=loop:
            cur=max(acm[:k])
        else:
            cur=(k//loop)*acm[-1]
            if k%loop>0:
                cur=max(cur,cur+max(acm[:k%loop]))
            else:
                cur-=acm[-1]
                cur+=max(acm)
    else:
        cur=max(acm[:min(k,loop)])
    
    ans=max(cur,ans)
    
print(ans)