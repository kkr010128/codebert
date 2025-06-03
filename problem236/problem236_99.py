from math import ceil


def main():
    width = int(input())
    height = int(input())
    lower_limit = int(input())
    print(ceil(lower_limit / max(width, height)))


if __name__ == '__main__':
    main()

