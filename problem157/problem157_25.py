import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (10 ** 6)
    ans = 0
    for i in range(n):
        if i - a[i] > 0:
            ans += b[i - a[i]]
        if i + a[i] < 10 ** 6:
            b[i + a[i]] += 1
    print(ans)


if __name__ == "__main__":
    main()
