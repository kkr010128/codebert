import math
import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    answer = 0
    for i in range(1, N):

        answer += A[math.floor(i / 2)]

    print(answer)


if __name__ == "__main__":
    main()
