def is_prime(n):# O(logn)
    if n == 2:
        return 1
    elif n == 1 or n % 2 == 0:
        return 0
    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            return 0
    return 1

X = int(input())

while True:
    if is_prime(X):
        print(X)
        exit()
    X += 1
