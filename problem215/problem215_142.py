# from math import sqrt
# from heapq import heappush, heappop
# from collections import deque
from functools import reduce

# a, b = [int(v) for v in input().split()]


def main():

    mod = 1000000007
    n, k = map(int, input().split())

    fact1 = [0] * (n + 1)  # 1/P!
    fact1[0] = 1

    for i in range(1, n + 1):
        fact1[i] = (fact1[i - 1] * i) % mod

    fact2 = [0] * (n + 1)  # P!
    fact2[n] = pow(fact1[n], mod-2, mod)

    for i in range(n, 0, -1):
        fact2[i - 1] = (fact2[i] * i) % mod

    def cmb2(n, r, mod):
        if r < 0 or r > n:
            return 0
        return fact1[n] * fact2[n - r] * fact2[r] % mod

    ans = 0
    for i in range(min(n - 1, k) + 1):
        ans += cmb2(n, i, mod) * cmb2(n - 1, i, mod)
        ans %= mod
    print(ans)


main()
