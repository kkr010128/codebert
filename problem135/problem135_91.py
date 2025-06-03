import math


def main() -> None:
    a, b = input().split()

    print((int(a)*int(b.replace('.', ''))) // 100)

    return


if __name__ == '__main__':
    main()
