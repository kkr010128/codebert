def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1
x = int(input())
while not is_prime(x):
    x += 1

print(x)