N=int(input())
mod=10**9+7
a = (10**N)%mod
b = (9**N)%mod
c = (8**N)%mod
ans = (a+c-2*b)%mod
print(ans)