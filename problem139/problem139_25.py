import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    H1, M1, H2, M2, K = map(int, input().split())
    if M2 >= M1:
        time = (H2 - H1) * 60 + M2 - M1
    else:
        time = (H2 - H1 - 1) * 60 + M2 + 60 - M1
    answer = max(time - K, 0)

    print(answer)


if __name__ == "__main__":
    main()
