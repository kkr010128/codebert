import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

X = int(input())
i = X

while 1:
    if not is_prime(i):
        i += 1
    else:
        ans = i
        print(i)
        break
