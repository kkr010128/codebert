def main():
    x = int(input())

    print((2000-x)//200 + 1 if x %200 != 0 else (2000-x)//200)


if __name__ == '__main__':
    main()
