n,k =list(map(int,input().split()))

mod = 10**9+7
ans = 1%mod
left_combination = 1
right_combination = 1

for i in range(1,min(k,n-1)+1):
    left_combination = (left_combination*(n+1-i)*pow(i,mod-2,mod))%mod
    right_combination = (right_combination*(n-i)*pow(i,mod-2,mod))%mod
    ans = (ans + (left_combination*right_combination)%mod)%mod

print(ans)