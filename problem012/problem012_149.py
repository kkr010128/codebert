import math
def is_prime(x):
    if x == 2:
        return True
    if (x % 2 == 0):
        return False
    m = math.ceil(math.sqrt(x))
    for i in range(3, m + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

prime = 0
for i in range(n):
    x = int(input())
    if is_prime(x):
        prime += 1

print(prime)