A,B,C,K=map(int,input().split())
ans=0
if A>K:
    ans+=K
else:
    ans+=A
    if B>K-A:
        ans+=0
    else:
        if (K-A-B)<C:
            ans+=-(K-A-B)
        else:
            ans+=-C
print(ans)