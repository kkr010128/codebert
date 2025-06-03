N, M = map(int, input().split())

def factorial(n):
    p = 1
    for i in range(n, 0, -1):
        p *= i
    return p


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


res = comb(M, 2) + comb(N, 2)

print(res)