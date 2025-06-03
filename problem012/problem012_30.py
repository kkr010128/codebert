from math import sqrt, floor


def is_prime(p):
    for i in range(2, floor(sqrt(p)) + 1):
        if not p % i:
            return False
    return True


n = int(input())
print(sum(is_prime(int(input())) for _ in range(n)))