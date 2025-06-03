def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 1 not in A:
        print(-1)
        exit()
    next = 1
    for a in A:
        if a == next:
            next += 1
    print(N - next + 1)


if __name__ == '__main__':
    main()
