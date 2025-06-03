N = int(input())
mod = 10 ** 9 +7
x = (10**N)%mod
y = (2*(9**N))%mod
z = (8**N)%mod
print((x-y+z)%mod)
