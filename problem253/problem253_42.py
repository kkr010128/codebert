import sys

input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    if (B - A) % 2 == 0:
        ans = (B - A) // 2
    else:
        a = (A - 1) + 1 + ((B - ((A - 1) + 1)) - 1) // 2
        b = (N - B) + 1 + (N - (A + ((N - B) + 1))) // 2
        ans = min(a, b)

    print(ans)


if __name__ == "__main__":
    main()
