N=int(input())
MOD=10**9+7

ans=10**N %MOD
ans=ans-2*9**N %MOD
ans=ans+8**N %MOD

print(ans%MOD)