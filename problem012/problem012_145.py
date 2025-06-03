import math

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n != 1

n = int(input())
answer = 0
for _ in range(0, n):
    m = int(input())
    if is_prime(m):
        answer = answer + 1
print(answer)
