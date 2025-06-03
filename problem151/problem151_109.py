def inverse_mod(a, mod=10**9+7):
    """ Calculate inverse of the integer a modulo mod.
    """
    return pow(a, mod-2, mod)


def combination_mod(n, r, mod=10**9+7):
    """ Calculate nCr modulo mod.
    """

    r = min(r, n-r)
    numerator = denominator = 1
    for i in range(r):
        numerator = numerator * (n - i) % mod
        denominator = denominator * (i + 1) % mod

    return numerator * inverse_mod(denominator, mod) % mod


def create_inverses_table(n, mod=10**9+7):
    """ Create table for inverses of the integers 0 to n modulo mod.
    """

    inv_table = [0] + [1] * n
    for x in range(2, n+1):
        inv_table[x] = -(mod//x) * inv_table[mod % x] % mod

    return inv_table


def solve():
    n_blocks, n_colors, n_max_pairs = map(int, input().split())

    if n_colors == 1:
        return int(n_blocks - n_max_pairs == 1)

    mod = 998244353

    inverses = create_inverses_table(max(n_colors, n_max_pairs), mod)

    e1 = n_colors * pow(n_colors-1, n_blocks-1, mod) % mod
    e2 = 1
    total = e1 * e2

    for k in range(1, n_max_pairs+1):
        e1 = e1 * inverses[n_colors - 1] % mod
        e2 = e2 * (n_blocks - k) * inverses[k] % mod
        total += e1 * e2
        total %= mod

    return total


def main():
    print(solve())


if __name__ == "__main__":
    main()
