import math


def main():
    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        ans += 1 if math.sqrt(x**2 + y**2) <= d else 0

    print(ans)


if __name__ == '__main__':
    main()
