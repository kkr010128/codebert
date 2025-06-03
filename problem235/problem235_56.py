from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

def prime_factorize(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
    return arr

primes = defaultdict(int)
for a in A:
    for x, p in prime_factorize(a):
        primes[x] = max(primes[x], p)
lcm = 1
for prime, ind in primes.items():
    lcm *= prime ** ind
ans = 0
for i in range(N):
    ans += lcm // A[i]
    if i == N // 2:
        ans %= mod
print(ans % mod)
