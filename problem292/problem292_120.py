def main():
    n = int(input())
    d_lst = list(map(int, input().split()))
    sum_d_lst = sum(d_lst)
    ans = 0

    for i in range(n):
        ans += d_lst[i] * (sum_d_lst - d_lst[i])

    print(ans // 2)


if __name__ == "__main__":
    main()
