import math
x=int(input())
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True
for i in range(x, 100003+1):
    if is_prime(i):
        print(i)
        exit()