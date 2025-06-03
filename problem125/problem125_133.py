def main():
    # n = int(input())
    # h, w, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    x = int(input())
    i = 1
    while (x*i) % 360 != 0:
        i += 1
    print(i)


if __name__ == '__main__':
    main()
