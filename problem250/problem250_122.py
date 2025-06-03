import math
X=int(input())

def is_prime(x):
    n = math.floor(math.sqrt(x))
    for i in range(2, n+1):
        if x % i == 0:
            return False
    return True

i = X
while True:
    if is_prime(i):
        print(i)
        break
    i += 1