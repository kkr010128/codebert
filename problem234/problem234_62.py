def main():
    N = int(input())

    ctr = [[0] * 10 for _ in range(10)]
    for x in range(1, N + 1):
        s = str(x)
        ctr[int(s[0])][int(s[-1])] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += ctr[i][j] * ctr[j][i]
    print(ans)


if __name__ == '__main__':
    main()
