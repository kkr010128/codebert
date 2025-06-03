import sys

input = sys.stdin.readline


def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    xyc = [0] * M
    for i in range(M):
        xyc[i] = map(int, input().split())

    ans = min(a) + min(b)
    for x, y, c in xyc:
        price = a[x - 1] + b[y - 1] - c
        if price < ans:
            ans = price

    print(ans)


if __name__ == "__main__":
    main()
