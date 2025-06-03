def solve():
    n, r = map(int, input().split())
    return r + max(0, 100 * (10-n))

print(solve())