import sys, math
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
x = int(lines.pop(0))

def iter_primes():
    _primes = []
    for n in range(2, 10 ** 6):
        is_prime = True
        upper_limit = math.floor(math.sqrt(n))
        for p in _primes:
            if n % p == 0:
                is_prime = False
                break
            if p >= upper_limit:
                break
        if is_prime:
            _primes.append(n)
            yield n

for n in iter_primes():
    if x <= n:
        print(n)
        break
