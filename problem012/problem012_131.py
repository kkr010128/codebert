def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

n = int(input())
cnt = 0
for _ in range(n):
    i = int(input())
    cnt += isPrime(i)

print(cnt)
