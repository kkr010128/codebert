def f(n):
    mod = 1000000007
    return (pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod

n = int(input())
print(f(n))
