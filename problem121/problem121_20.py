def solve(n):
    import math
    m = 26
    nn = n - 1
    for i in range(1, m + 1):
        p = m ** i
        if p > nn:
            break
        nn -= p
    s = ''
    for j in range(1, i + 1):
        p = m ** (i - j)
        x, nn = divmod(nn, p)
        s += chr(x + ord('a'))
    return s

def main(istr, ostr):
    n, = list(map(int, istr.readline().strip().split()))
    result = solve(n)
    print(result, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)
