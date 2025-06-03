n,k = map(int,input().split())
mod = 10**9+7
num_gcd = [0]*(k+1)
for i in range(1,k+1)[::-1]:
    num = pow(k//i,n,mod)
    for j in range(2,k//i+1):
        num -= num_gcd[i*j]
    if num < 0:
        num += mod
    num_gcd[i] = num
ans = 0
for i in range(1,k+1):
    ans += i*num_gcd[i]
    ans %= mod
print(ans)