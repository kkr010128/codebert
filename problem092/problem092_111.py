x,k,d=map(int,input().split())
x=abs(x)
if x//d <=k:
    ans=x%d
    if (k-x//d)%2==1:
        ans=abs(ans-d)
    print(ans)
else:
    ans=x-d*k
    print(ans)