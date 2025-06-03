def isPrime(n):
    for i in range(2, n):
        if i * i > n:
            return 1
        if n % i == 0:
            return 0
    return 1
 
ans = 0
n = int(input())
for i in range(n):
    x = int(input())
    ans = ans + isPrime(x)
 
print(ans)
