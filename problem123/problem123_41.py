import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = 0
    for a in A:
        B ^= a

    ans = []
    for a in A:
        ans.append(a ^ B)

    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
