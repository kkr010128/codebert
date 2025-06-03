x = int(input())
n = 10 * x
primes = [True] * n
for i in range(2, n):
    if primes[i]:
        for j in range(i * i, n, i):
            primes[j] = False

for i in range(x, n):
    if primes[i]:
        print(i)
        exit()
