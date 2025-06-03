def solve():
    from math import gcd
    n, k = map(int, input().split())
    print(n * k // gcd(n, k))


solve()
