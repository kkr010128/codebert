import sys

input = sys.stdin.readline


def main():
    N = int(input())

    if N % 2 == 0:
        ans = (N - 2) // 2
    else:
        ans = (N - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
