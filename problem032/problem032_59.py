def main():
    input()
    x, y = [list(map(int, input().split())) for _ in range(2)]
    for p in (1, 2, 3):
        distance = (sum(map(lambda i: i ** p, [abs(xi - yi) for xi, yi, in zip(x, y)]))) ** (1/p)
        print('{:.5f}'.format(distance))
    distance = max([abs(xi - yi) for xi, yi in zip(x, y)])
    print('{:.5f}'.format(distance))


if __name__ == '__main__':
    main()

