def main():
    _ = int(input())
    A = [int(i) for i in input().split()]
    ans = 1
    if 0 in A:
        ans = 0
    else:
        for a in A:
            ans *= a
            if (10**18 < ans):
                ans = -1
                break
        if (10**18 < ans):
            ans = -1

    print(ans)


if __name__ == '__main__':
    main()
