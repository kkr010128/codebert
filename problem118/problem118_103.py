def solve(string):
    n = int(string)
    return str(sum(i * (n // i) * (n // i + 1) // 2 for i in range(1, n + 1)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
