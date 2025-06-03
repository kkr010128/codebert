N=int(input())
A=list(map(int,input().split()))
mod=10**9+7

def gcd(a, b):
    if a == 0:
        return b
    else:
        g = gcd(b % a, a)
        return g

lcm=1

for a in A:
    lcm=lcm*a//gcd(a,lcm)

ans=0

for a in A:
    ans+=(lcm*pow(a,mod-2,mod))%mod
    ans%=mod

print(ans)