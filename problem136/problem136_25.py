from math import sqrt


def eratosthenes(x):
    prime = []
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            prime.append(i)
            while x % i == 0:
                x //= i
    
    return prime


N = int(input())
prime = eratosthenes(N)
ans = 0
for x in prime:
    i = 1
    while N % x**i == 0:
        ans += 1
        N //= x**i
        i += 1
    while N % x == 0:
        N //= x

if N > 1:
    ans += 1
print(ans)