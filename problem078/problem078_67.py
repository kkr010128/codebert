n = int(input())
mod=10**9+7

if n==1:
    print(0)
else:
    print(((10**n)-(9**n)-(9**n)+(8**n))%mod)
