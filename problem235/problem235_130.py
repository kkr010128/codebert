
from fractions import gcd

N=int(input())
A=list(map(int, input().split()))

p=10**9+7
n = 10 ** 6  # N は必要分だけ用意する
#fact = [1, 1]  # fact[n] = (n! mod p)
#factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用 逆元

for i in range(2, n + 1):
    #fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    #factinv.append((factinv[-1] * inv[-1]) % p)
#a//gcd(a,b)*b

def lcm(a,b):
    g=gcd(a,b)
    #return ((a*b)*pow(g,p-2,p))%p
    return a//gcd(a,b)*b

LCM=1
for x in A:
    LCM=lcm(LCM,x)



#print(LCM)
ans=0
LCM%=p
for i in range(N):
    ans+=(LCM*inv[A[i]])%p
    #ans+=(LCM*pow(A[i],p-2,p))%p
    ans%=p
print(ans)