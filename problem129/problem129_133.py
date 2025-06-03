def solve(ls):
    n = len(ls)
    lim = max(ls)
    sieve = [1] * (lim + 1)
    result = 0
    ls.sort()
    for i in range(n):
        x = ls[i]
        if sieve[x] == 0:
            continue
        # Don't count if ls[i] = ls[i+1]
        if not (i + 1 < n and x == ls[i + 1]):
            result += 1
        y = x
        while y <= lim:
            sieve[y] = 0
            y += x
    return result


def main(istr, ostr):
    n = list(map(int, istr.readline().strip().split()))
    ls = list(map(int, istr.readline().strip().split()))
    result = solve(ls)
    print(result, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)
