def prime_fact(n):
    primes = []
    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt:
            primes.append([i, cnt])
        i += 1

    if n != 1:
        primes.append([n, 1])
    return primes

a, b = map(int, input().split())

if b < a:
    a, b = b, a

fact = prime_fact(a)
ans = 1
for i, j in fact:
    if b % i == 0:
        ans += 1
if a == 1:
    ans = 1

print(ans)