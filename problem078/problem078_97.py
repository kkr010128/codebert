N = int(input())
if N == 1:
    print(0)
else:
    mod = 10**9+7
    print((10**N - (2*(9**N) - 8**N)) % mod)
