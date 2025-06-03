# coding: utf-8
from math import sqrt


def solve(*args: str) -> str:
    k = int(args[0])

    l = 9*(k//7 if 0 == k % 7 else k)
    if 0 == l % 2 or 0 == l % 5:
        return '-1'

    r = phi = l
    for i in range(2, int(sqrt(l)+1)):
        if 0 == r % i:
            phi = phi*(i-1)//i
            while 0 == r % i:
                r //= i
    if 1 < r:
        phi = phi*(r-1)//r

    D = set()
    for d in range(1, int(sqrt(phi)+1)):
        if 0 == phi % d:
            D.add(d)
            D.add(phi//d)

    ret = -1
    for m in sorted(D):
        if 1 == pow(10, m, l):
            ret = m
            break

    return str(ret)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
