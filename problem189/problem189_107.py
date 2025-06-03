from math import factorial

N, M = map(int, input().split())

if N <= 1:
    combN = 0
else:
    combN = factorial(N) // (factorial(N - 2) * factorial(2))

if M <= 1:
    combM = 0
else:
    combM = factorial(M) // (factorial(M - 2) * factorial(2))

print(combN + combM)
