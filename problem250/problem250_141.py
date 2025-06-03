# エラトステネスの篩
# https://qiita.com/takayg1/items/3769ab4cc62a231f4259

def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

MAX_N=(10**6)
Primes = eratosthenes_sieve(MAX_N)

x = int(input())
while True:
    if Primes[x]:
        print(x)
        exit()
    x += 1