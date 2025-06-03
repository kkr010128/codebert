def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
n = int(input())
ans = 0

for i in range(n):
    t = int(input())
    if isPrime(t):
        ans += 1
print(ans)