# coding: utf-8


def solve(*args: str) -> str:
    n, m, k = map(int, args[0].split())
    mod = 998244353

    if m == 1 and n-1 == k:
        return str(1)

    ncr = 1
    p = m*pow(m-1, n-1, mod) % mod

    ret = p
    iR = [1]*(k+1)
    im = pow(m-1, mod-2, mod)

    for i in range(1, k+1):
        iR[i] = max(1, (-(mod//i) * iR[mod % i]) % mod)
        ncr = (ncr * (n-i)*iR[i]) % mod
        p = (p*im) % mod
        ret += p*ncr % mod

    return str(ret % mod)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
