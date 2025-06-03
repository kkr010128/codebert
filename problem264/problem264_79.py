import sys

input = sys.stdin.readline


def main():
    M1, D1 = map(int, input().split())
    M2, D2 = map(int, input().split())

    if M1 == M2:
        ans = 0
    else:
        ans = 1

    print(ans)


if __name__ == "__main__":
    main()
