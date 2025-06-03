def gcd(a, b):
    """calculate the greatest common divisor of a, b

    >>> gcd(54, 20)
    2
    >>> gcd(147, 105)
    21
    >>> gcd(100000002, 39273000)
    114
    """
    if a > b:
        a, b = b, a

    if a == 0:
        return b

    return gcd(b % a, a)


def run():
    a, b = [int(i) for i in input().split()]
    print(gcd(a, b))


if __name__ == '__main__':
    run()

