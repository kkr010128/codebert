import math


def is_prime(n):
    global primes
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s = int(math.sqrt(n))
    for x in range(3, s + 1, 2):
        if n % x == 0:
            return False
    else:
        return True


N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()
print([is_prime(x) for x in d].count(True))