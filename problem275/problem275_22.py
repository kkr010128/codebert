def main():
    X, Y = map(int, input().split())

    ans = 0;

    if X == 1:
        ans += 300000
    elif X == 2:
        ans += 200000
    elif X == 3:
        ans += 100000

    if Y == 1:
        ans += 300000
    elif Y == 2:
        ans += 200000
    elif Y == 3:
        ans += 100000

    if X == 1 and Y == 1:
        ans += 400000

    print(ans)
if __name__ == '__main__':
    main()