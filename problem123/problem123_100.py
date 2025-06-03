def solve(ls):
    n = len(ls)
    s = 0
    for i in range(n):
        s ^= ls[i]

    result = [0] * n
    for i in range(n):
        result[i] = s ^ ls[i]
    return result


def main(istr, ostr):
    (n,) = list(map(int, istr.readline().strip().split()))
    ls = list(map(int, istr.readline().strip().split()))
    result = solve(ls)
    print(*result, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)
