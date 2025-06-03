def main():
    K, X = map(int, input().split())

    if 500 * K >= X:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
