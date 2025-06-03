def main():
    x, y = map(int, input().split())
    mul_xy = x * y
    while True:
        x, y = y, x % y
        if not y:
            break
    print(int(mul_xy / x))

if __name__ == '__main__':
    main()
