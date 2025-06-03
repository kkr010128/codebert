def main():
    x = int(input())

    for i in range(x + 1):
        if 0 <= x - 100 * i <= 5 * i:
            print(1)
            exit()
    else:
        print(0)


if __name__ == "__main__":
    main()
