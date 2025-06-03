def solve(string):
    n, k = 7, int(string)
    if k % 2 == 0 or k % 5 == 0:
        return "-1"
    for i in range(k):
        if not n % k:
            return str(i + 1)
        n = (10 * n + 7) % k


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
