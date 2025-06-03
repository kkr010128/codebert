n = int(input())
mod = 7+10**9
a = 10**n % mod
b = 9**n % mod
c = 8**n % mod
print((a - 2*b + c)%mod)