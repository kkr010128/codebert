import math


def main():
    N = int(input())

    if N % 2 == 0:
        print("{:.11f}".format((N / 2) / N))
    else:
        print("{:.11f}".format(math.ceil(N / 2) / N))


if __name__ == "__main__":
    main()
