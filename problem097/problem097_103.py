def solve(string):
    k = int(string)
    if k % 2 == 0 or k % 5 == 0:
        return "-1"
    n = 7
    ans = 1
    while n % k:
        n = (10 * n + 7) % k
        ans += 1
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
