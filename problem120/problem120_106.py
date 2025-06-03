def solve(string):
    n, k, *p = map(int, string.split())
    p = sorted(p)
    return str(sum(p[:k]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
