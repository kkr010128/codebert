X = int(input())
primes = [1] * (10 ** 6) 
n = 1
primes[0] = 0
primes[1] = 0
while True:
    n += 1
    if primes[n] == 0:
        continue
    if n >= X:
        print(n)
        break
    i = 2
    while i * n < len(primes):
        primes[i * n] = 0
        i += 1
