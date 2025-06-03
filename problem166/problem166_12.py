from collections import Counter


def main():
    MOD = 2019
    s = input()
    n = len(s)
    t = [0] * (n + 1)
    # n-1,n-2,...,0
    for i in range(n - 1, -1, -1):
        t[i] = t[i + 1] + pow(10, n - i - 1, MOD) * int(s[i])
        t[i] %= MOD
    c = Counter(t)
    cnt = 0
    for v in c.values():
        cnt += v * (v - 1) // 2
    print(cnt)


if __name__ == '__main__':
    main()
