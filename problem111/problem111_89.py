def main():
    n = int(input())
    a_list = sorted(list(map(int, input().split())), reverse=True)
    ans = a_list[0]

    cnt = 1
    i = 1
    while True:
        if cnt >= n - 2:
            break
        ans += a_list[i] * 2
        i += 1
        cnt += 2

    if cnt == n - 2:
        ans += a_list[i]

    print(ans)


if __name__ == "__main__":
    main()
