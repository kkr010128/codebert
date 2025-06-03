def main():
    n = int(input())
    d_lst = list(map(int, input().split()))
    ans = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += d_lst[i] * d_lst[j]

    print(ans)


if __name__ == "__main__":
    main()
