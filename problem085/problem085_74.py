N = int(input())
A = list(map(int,input().split()))

M = 10**6

import math

setwise = A[0]
for i in range(1,N):
    setwise = math.gcd(setwise,A[i])
    
PrimeFactorss = [[] for _ in range(M+1)]
for i in range(2, M+1):
    if len(PrimeFactorss[i]) == 0:
        for x in range(i, M+1, i):
            PrimeFactorss[x].append(i)
num_list = [0]*(M+1)

for i in range(N):
    num_list[A[i]] += 1

pairwise = [0]*(M+1)

n=M
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes=list(primes)

for i in primes:
    for j in range(i,M+1,i):
        if num_list[j]==1:
            pairwise[i] += 1
        
ans = 0    
for i in pairwise:
    if i>1:
        ans += 1
        break
    
if setwise == 1 and ans == 0:
    print("pairwise coprime")
elif setwise == 1:
    print("setwise coprime")
else:
    print("not coprime")

