n = int(input())

def sieve1(n):
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2*2, n+1, 2):
        isPrime[i] = False
    for i in range(3, n+1):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j] = False
    return isPrime
numOfDivisors = [2] * (n+1)
numOfDivisors[1] = 1
numOfDivisors[0] = 0
isPrime = sieve1(n)
for i in range(2, n+1):
    if isPrime[i]:
        for j in range(2*i, n+1, i):
            x = j // i
            numOfDivisors[j] += numOfDivisors[x] - 1
ans = 0
for k in range(1, n+1):
    ans += numOfDivisors[k] * k
print (ans)