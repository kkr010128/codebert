# coding: utf-8


def solve(*args: str) -> str:
    k = int(args[0])

    l = 9*(k//7 if k % 7 == 0 else k)
    if l % 2 == 0 or l % 5 == 0:
        return '-1'

    r = phi = l
    for i in range(2, int(-pow(l, 1/2))):
        if r % i == 0:
            phi = phi//i*(i-1)
            while r % i:
                r //= i

    a = 10 % l
    ret = 1
    while(a != 1):
        a = a*10 % l
        ret += 1
        if phi < ret:
            ret = -1
            break

    return str(ret)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
