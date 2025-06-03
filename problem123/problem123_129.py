import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = 0
    for a in A:
        S = S ^ a
    answer = []
    for a in A:
        answer.append(S ^ a)
    print(*answer)


if __name__ == "__main__":
    main()
