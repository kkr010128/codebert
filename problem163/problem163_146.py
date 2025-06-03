def main():
    s, w = map(int, input().split())

    if s <= w:
        ans = 'unsafe'
    else:
        ans = 'safe'

    print(ans)


if __name__ == "__main__":
    main()
