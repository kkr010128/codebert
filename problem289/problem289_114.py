def main():
    import math
    a, b, x = map(int, input().split())
    if a * a * b >= x * 2:
        c = x * 2 / (b * a)
        print(math.degrees(math.atan(b / c)))
    else:
        d = 2 * (b - x / a / a)
        print(math.degrees(math.atan(d / a)))


if __name__ == '__main__':
    main()
