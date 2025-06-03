n,k=map(int,input().split())

if n>=k:
    n%=k

ans=min(n,k-n)

print(ans)