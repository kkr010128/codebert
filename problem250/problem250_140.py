x = int(input())

import math

def check(n):
    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = x
while check(n) == False:
    n += 1

print(n)
