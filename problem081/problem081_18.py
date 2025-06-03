def solve(string):
    d, t, s = map(int, string.split())
    return "Yes" if d <= t * s else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
