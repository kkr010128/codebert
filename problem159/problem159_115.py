def main():
    X = int(input())
    v = 100
    ans = 0
    while v < X:
        ans += 1
        v = int(v * 101 // 100)
    print(ans)


if __name__ == '__main__':
    main()
