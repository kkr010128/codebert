def main():
    day = [list(map(int, input().split())) for _ in range(2)]
    print(1 if day[0][0] + 1 == day[1][0] else 0)


if __name__ == '__main__':
    main()

