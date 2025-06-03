n=int(input())
ans=10**n
ans-=2*9**n
ans+=8**n
ans%=10**9+7
print(ans)