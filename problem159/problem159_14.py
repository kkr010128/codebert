def main():
    x = int(input())
    now = 100
    ans = 0

    while True:
        now = now * 101 // 100
        ans += 1
        if now >= x:
            break

    print(ans)


if __name__ == "__main__":
    main()
