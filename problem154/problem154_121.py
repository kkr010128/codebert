def main():
    n, k = map(int, input().split())
    d_lst = [0 for _ in range(k)]
    a_lst = [0 for _ in range(k)]

    for i in range(k):
        d_lst[i] = int(input())
        a_lst[i] = list(map(int, input().split()))

    snuke_lst = [0 for _ in range(n)]

    for i in range(k):
        for a in a_lst[i]:
            snuke_lst[a - 1] = 1

    ans = n - sum(snuke_lst)

    print(ans)


if __name__ == "__main__":
    main()
