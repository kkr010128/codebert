def main():
    a = list(map(int, input().split()))
    D = a[0]
    T = a[1]
    S = a[2]
    time = D / S
    print("Yes" if time <= T else "No")


if __name__ == '__main__':
    main()
