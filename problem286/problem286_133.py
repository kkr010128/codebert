def main():
    a, b = map(int, input().split())
    if 10 > a and 10 > b:
        print(a*b)
    else:
        print("-1")


if __name__ == '__main__':
    main()
