def main():
    n, k = map(int, input().split())
    h_list = list(map(int, input().split()))
    h_list.sort(reverse=True)

    if n <= k:
        ans = 0
    else:
        ans = sum(h_list[k:])

    print(ans)


if __name__ == "__main__":
    main()
