import math

n = int(input())

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
i = 1
while i > 0:
    if is_prime(n):
        break
    n += 1 
print (n)