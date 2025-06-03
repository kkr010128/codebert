def isprime(n):
    if n < 2: return 0
    elif n == 2: return 1

    if n % 2 == 0: return 0

    for i in range(3, n, 2):
        if i > n/i: return 1
        if n % i == 0 : return 0

    return 1

N = int(input())
n = [int(input()) for i in range(N)]

a = [i for i in n if isprime(i)]

print(len(a))
