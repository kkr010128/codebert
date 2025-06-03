def main():
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    total = sum(a_lst)
    cnt = 0

    for a in a_lst:
        if a * 4 * m >= total:
            cnt += 1

    if cnt >= m:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
