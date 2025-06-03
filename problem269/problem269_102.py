import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    A = A1 * T1 + A2 * T2
    B = B1 * T1 + B2 * T2

    if A1 < B1 and A < B:
        print(0)
        return

    if A1 > B1 and A > B:
        print(0)
        return

    if A == B:
        print("infinity")
        return

    # T1 + T2 分後にできる差
    diff = abs(A - B)

    if T1 * abs(A1 - B1) % diff == 0:
        ans = T1 * abs(A1 - B1) // diff * 2
    else:
        ans = T1 * abs(A1 - B1) // diff * 2 + 1

    print(ans)


if __name__ == "__main__":
    main()
