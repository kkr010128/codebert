def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

result = 0
for i in range(int(input())):
    result += isprime(int(input()))
print(result)