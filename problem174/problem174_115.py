import math


def abc162c_sum_of_gcd_of_tuples():
    k = int(input())
    total = 0
    memo = [[-1] * k for _ in range(k)]
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            if memo[a - 1][b - 1] == -1:
                memo[a - 1][b - 1] = math.gcd(a, b)
            g = memo[a - 1][b - 1]
            for c in range(1, k + 1):
                if memo[g - 1][c - 1] == -1:
                    memo[g - 1][c - 1] = math.gcd(g, c)
                total += memo[g - 1][c - 1]
    print(total)

abc162c_sum_of_gcd_of_tuples()