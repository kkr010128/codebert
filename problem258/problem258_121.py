import sys
input = sys.stdin.readline

n, x, res = int(input()), 1, 0
if n & 1: print(0)
else:
    n //= 2
    while x < n:
        x *= 5
        res += n // x
    print(res)