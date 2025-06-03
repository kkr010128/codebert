def solve(string):
    x, k, d = map(int, string.split())
    x = abs(x)
    if k % 2:
        x = min(x - d, x + d, key=abs)
        k -= 1
    k, d = k // 2, d * 2
    if x < k * d:
        return str(min(x % d, abs((x % d) - d)))
    else:
        return str(x - k * d)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
