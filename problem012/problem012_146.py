def isprime(n):
    divider = 2
    while divider ** 2 <= n:
        if n % divider == 0:
            return False
        divider += 1
    return True

result = 0
n = int(input())
for n in range(n):
    result += isprime(int(input()))
print(result)