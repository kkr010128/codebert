N=int(input())
A=list(map(int,input().split()))

#素数
def primes(n):
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2, 3] + [3*i+1|1 for i in range(1, n//3-correction) if sieve[i]]

primes=primes(int(1000))
points=[0]*1000001

from math import gcd
pairprime_flag=True
allgcd=A[0]
allprime=set()

for a in A:
    allgcd=gcd(allgcd,a)
    if pairprime_flag:
        for i in primes:
            if a%i==0:
                if points[i]==1:
                    pairprime_flag=False
                points[i]=1
                while a%i==0:
                    a//=i
            if a==1:
                break
        if a!=1:
            if points[a]!=0:
                pairprime_flag=False
            else:
                points[a]=1

if pairprime_flag:
    print('pairwise coprime')
elif allgcd==1:
    print('setwise coprime')
else:
    print('not coprime')
