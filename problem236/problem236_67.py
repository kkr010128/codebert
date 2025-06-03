import sys

input = sys.stdin.readline


def main():
    H = int(input())
    W = int(input())
    N = int(input())

    q, r, = divmod(N, max(H, W))
    ans = q
    ans += 1 if r > 0 else 0

    print(ans)


if __name__ == "__main__":
    main()
