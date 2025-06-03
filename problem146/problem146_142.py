MOD = 10**9 + 7
P = 7 ** 21 + 52


def F(a, b):
    return (a * pow(b, P-2, P)) % P


def main():
    from collections import Counter
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    T = [[int(i) for i in input().split()] for j in range(N)]
    cnt_zero = [0, 0]  # 片方が0のとき
    p = 0  # 両方0
    cA = Counter()
    B = []
    used = set()
    for a, b in T:
        if a == 0 and b == 0:
            p += 1
        elif a == 0:
            cnt_zero[0] += 1
        elif b == 0:
            cnt_zero[1] += 1
        else:
            x = F(a, b)
            y = -F(b, a) % P
            cA[x] += 1
            if x not in used and y not in used:
                B.append((x, y))
                used.add(x)
                used.add(y)

    ans = 1
    ans *= pow(2, cnt_zero[0], MOD) - 1 + pow(2, cnt_zero[1], MOD) - 1 + 1
    for a, b in B:
        ans *= pow(2, cA[a], MOD) - 1 + pow(2, cA[b], MOD) - 1 + 1
        ans %= MOD
    print((ans + p - 1) % MOD)


if __name__ == '__main__':
    main()
