N = int(input())
X = input()

memo = {}


def popcount(n):
    return bin(n).count('1')


def f(n):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = 1 + f(n % popcount(n))
    return memo[n]


def solve(N, X):
    Xint = int(X, 2)
    p = popcount(Xint)
    if 1 < p:
        x1 = Xint % (p - 1)
    x2 = Xint % (p + 1)
    ans = []
    b = 1
    if 1 < p:
        bmod1 = b % (p - 1)
    bmod2 = b % (p + 1)
    for i in range(N):
        if X[-1 - i] == '1':
            if 1 < p:
                ans.append(1 + f((x1 - bmod1) % (p - 1)))
            else:
                ans.append(0)
        else:
            ans.append(1 + f((x2 + bmod2) % (p + 1)))
        b <<= 1
        if 1 < p:
            bmod1 = bmod1 * 2 % (p - 1)
        bmod2 = bmod2 * 2 % (p + 1)

    return list(reversed(ans))


for x in solve(N, X):
    print(x)