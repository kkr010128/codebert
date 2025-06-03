n,a,b = list(map(int, input().split()))
if abs(b-a)%2==0:
    print(abs(b-a)//2)
else:
    #卓1に行くコスト
    c1=max(a,b)-1
    #卓Nに行くコスト
    c2=n-min(a,b)
    
    ans=0
    cost=min(c1,c2)
    if c1<c2:
        ans+=min(a,b)-1
    else:
        ans+=n-max(a,b)
    cost-=ans
    ans+=(cost+1)//2
    print(ans)