def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    op = 0
    while True:
        new = [0 for _ in range(n + 1)]
        for i in range(n):
            new[max(0, i - a[i])] += 1
            new[min(n, i + a[i] + 1)] -= 1
        for i in range(1, n + 1):
            new[i] += new[i - 1]
        a = new[:-1]
        op += 1
        if op == k or all(aa == n for aa in a):
            break
    print(" ".join(map(str, a)))


if __name__ == '__main__':
    main()
