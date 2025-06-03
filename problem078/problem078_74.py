n = int(input())
mod = 10**9+7
a = pow(10,n,mod)
b = pow(9,n,mod)
c = pow(9,n,mod)
d = pow(8,n,mod)
print((a-b-c+d)%mod)