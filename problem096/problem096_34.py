def solve(string):
    n, d, *xy = map(int, string.split())
    return str(sum([1 if x**2 + y**2 <= d**2 else 0 for x, y in zip(*[iter(xy)] * 2)]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
