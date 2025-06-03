def main(x):
    for i in range(9):
        _min = 2000 - (200 * (i + 1))
        if _min <= x:
            print(i + 1)
            return


if __name__ == "__main__":
    x = int(input())

    main(x)
