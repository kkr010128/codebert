def main():
    A1, A2, A3 = map(int, input().split())

    if A1 + A2 + A3 >= 22:
        ans = "bust"
    else:
        ans = "win"

    print(ans)


if __name__ == "__main__":
    main()
