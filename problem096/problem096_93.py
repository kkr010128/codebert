import sys
input = sys.stdin.readline


def main():
    N, D = map(int, input().split())
    D = D ** 2
    ans = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        if X ** 2 + Y ** 2 <= D:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()