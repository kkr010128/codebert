import sys

read = sys.stdin.buffer.read
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    M = 60

    ans = 0
    p = 1
    for _ in range(M):
        n = 0
        for i, a in enumerate(A):
            if not a:
                continue
            A[i], d = a // 2, a % 2
            if d:
                n += 1
        ans = (ans + n * (N - n) * p) % MOD
        p = p * 2 % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
