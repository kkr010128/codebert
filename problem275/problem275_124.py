import sys

input = sys.stdin.readline


def main():
    X, Y = map(int, input().split())

    ans = 0
    for i in [X, Y]:
        if i == 1:
            ans += 300000
        elif i == 2:
            ans += 200000
        elif i == 3:
            ans += 100000

    if X == Y == 1:
        ans += 400000

    print(ans)


if __name__ == "__main__":
    main()
