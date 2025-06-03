def main():
    N = int(input())
    A = [[i for i in input().split()] for j in range(N)]
    X = input()
    ans = 0
    flag = False
    for a, b in A:
        if a == X:
            flag = True
            continue
        if flag:
            ans += int(b)
    print(ans)


if __name__ == '__main__':
    main()
