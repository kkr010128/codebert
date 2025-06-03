def is_prime(x):
    if x == 2:
        return True
    if (x < 2) or (x%2 == 0):
        return False
    return all(x%i for i in xrange(3, int(x**(0.5) + 1), 2))

N = input()
print sum(is_prime(input()) for i in range(N))