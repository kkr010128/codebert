def main():
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    total = sum(a_lst)

    if total > n:
        ans = -1
    else:
        ans = n - total

    print(ans)


if __name__ == "__main__":
    main()
