n=int(input())
mod=10**9+7
ans=10**n
ans-=2*(9**n)
ans+=8**n
ans%=mod
print(ans)
