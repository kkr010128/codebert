def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    N = int(n ** 0.5)
    for i in range(5, N + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
ans = 0
for _ in range(N):
    a = int(input())
    ans += 1 if isPrime(a) else 0
print(ans)