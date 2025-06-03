def main():
    n, k = map(int, input().split())
    h_lst = list(map(int, input().split()))
    ans = 0

    for h in h_lst:
        if h >= k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
