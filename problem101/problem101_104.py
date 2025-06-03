import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    A, B, C = [int(x) for x in input().split()]
    K = int(input())

    cnt = 0

    while A >= B:
        cnt += 1
        B *= 2

    while B >= C:
        cnt += 1
        C *= 2

    if cnt <= K:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

