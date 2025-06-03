def main():
    n = int(input())
    dss = [list(map(int, input().split())) for _ in range(n)]

    ans = "No"
    Count = 0
    for ds in dss:
        if ds[0] == ds[1]:
            Count += 1
        else:
            Count = 0
        if Count == 3:
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
