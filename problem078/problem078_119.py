n = int(input())
mod = 1000000007
if n < 2:
    print(0)
else:
    print((pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod)