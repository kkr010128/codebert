
def main():
    n = int(input())
    # a, b, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    # s = input()
    mx = 0
    result = 0
    for num in a:
        mx = max(mx, num)
        if mx > num:
            result += mx - num
    print(result)


if __name__ == '__main__':
    main()
