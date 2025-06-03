# coding: utf-8


def solve(*args: str) -> str:
    n = int(args[0])
    A = list(map(int, args[1].split()))

    rem = sum(A)
    cur = 1
    ret = 0
    for a in A:
        cur = min(rem, cur)
        rem -= a
        ret += cur
        cur = 2*(cur-a)
        if cur < 0:
            ret = -1
            break

    return str(ret)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
