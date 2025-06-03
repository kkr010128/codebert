def solve(string):
    n, *a = map(int, string.split())
    a = sorted(a, reverse=True)
    ans = sum(a[:(n + 1) // 2]) * 2 - a[0]
    ans -= a[(n + 1) // 2 - 1] if n % 2 else 0
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
