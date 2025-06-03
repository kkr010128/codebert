def main():
    n = int(input())
    l = list(map(int, input().split()))

    if 0 in l:
        print(0)
        return

    prod = 1
    for i in l:
        prod *= i
        if prod > 1000000000000000000:
            print(-1)
            return

    print(prod)

if __name__ == '__main__':
    main()