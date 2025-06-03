import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(0, n, 2):
        ans += a[i] % 2 == 1
    print(ans)


if __name__ == "__main__":
    main()
