from fractions import gcd


def factor(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        res.append(n)
    return res


A, B = map(int, input().split())
g = gcd(A, B)
print(len(set(factor(g))) + 1)
