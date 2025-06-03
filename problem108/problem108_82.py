def main():
    n = int(input())

    if n % 1000 == 0:
        print(0)
    else:
        print(1000 - int(n%1000))


if __name__ == '__main__':
    main()
