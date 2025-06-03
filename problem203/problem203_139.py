from math import floor


def main():
    a, b = map(int, input().split())
    for yen in range(1, 1100):
        if floor(yen * 0.08) == a and floor(yen * 0.1) == b:
            print(yen)
            return
    print(-1)


if __name__ == '__main__':
    main()
