import math


def main():
    n = int(input())
    # n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    ans = 0

    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)


if __name__ == '__main__':
    main()
