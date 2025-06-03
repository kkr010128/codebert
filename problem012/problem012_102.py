def prime_numbers(n):
    cnds = [True] * n
    for x in xrange(2, int(n**0.5 + 1)):
        if cnds[x]:
            for m in xrange(2*x, n, x):
                cnds[m] = False
    return [i for i in xrange(2, n) if cnds[i]]

def is_prime(n):
    return all(n % m for m in primes if m < n)

primes = prime_numbers(10**4)
N = input()
print sum(is_prime(input()) for i in range(N))