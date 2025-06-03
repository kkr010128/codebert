n,k=map(int,input().split())
ans=n%k

if ans>k//2:
    print(abs(ans-k))
elif ans<=k//2:
    print(ans)