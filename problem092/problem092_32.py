def solve(string):
    x, k, d = map(int, string.split())
    if k % 2:
        x = min(x - d, x + d, key=abs)
        k -= 1
    x, k, d = abs(x), k // 2, d * 2
    return str(min(x % d, abs((x % d) - d))) if x < k * d else str(x - k * d)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
