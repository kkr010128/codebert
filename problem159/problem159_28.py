def main():
    X = int(input())
    ans = 0
    money = 100

    while money < X:
        ans += 1
        money = money * 101 // 100

    print(ans)


if __name__ == '__main__':
    main()