def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True

N = int(input())
cnt = 0

for _ in range(N):
    a = int(input())
    if isPrime(a):
        cnt += 1

print(cnt)