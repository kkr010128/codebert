def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    memo = [0] * (n + 1)
    for _ in range(k):
        flag = True
        for i, aa in enumerate(a):
            bf = (i - aa if i - aa >= 0 else 0)
            af = (i + aa + 1 if i + aa < n else n)
            memo[bf] += 1
            memo[af] -= 1
        for i in range(n):
            memo[i + 1] += memo[i]
            a[i] = memo[i]
            if a[i] != n:
                flag = False
            memo[i] = 0
        if flag:
            break
    print(*a)


if __name__ == '__main__':
    main()
