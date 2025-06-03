import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X, Y, A, B, C, *PQR = map(int, read().split())
    P = PQR[:A]
    Q = PQR[A : A + B]
    R = PQR[A + B :]

    P.sort(reverse=True)
    Q.sort(reverse=True)

    vec = P[:X] + Q[:Y] + R
    vec.sort(reverse=True)
    ans = sum(vec[: X + Y])

    print(ans)
    return


if __name__ == '__main__':
    main()
