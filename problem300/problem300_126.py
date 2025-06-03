import math
from functools import reduce


def prime_factorize(n):
    """素因数分解する。"""
    def facs(n):
        """試し割り法における割る数を生成する。"""
        yield 2
        max_prime = int(pow(n, 0.5)) + 2
        for x in range(3, max_prime, 2):
            yield x

    ans = set()
    for fac in facs(n):
        if n % fac == 0:
            ans.add(fac)
            while n % fac == 0:
                n //= fac
    if n != 1:
        ans.add(n)
    return ans


def gcd_list(numbers):
    # これじゃすべての最大公約数を出しているだけ。
    # すべての組み合わせにおいて最大公約数が1でなくてはいけない。
    return reduce(math.gcd, numbers)


def main():
    a, b = [int(x) for x in input().split()]
    gcd_ = math.gcd(a, b)
    primes = prime_factorize(gcd_)
    print(len(primes) + 1)


if __name__ == '__main__':
    main()
