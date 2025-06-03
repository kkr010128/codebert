import math

def main():
    a, b, x = map(int, input().split())
    if x < a * a * b / 2:
        tan = 2 * x / (b * b * a)
        print(90 - math.degrees(math.atan(tan)))
    else:
        tan = (2 / a) * (b - x / a**2)
        print(math.degrees(math.atan(tan)))


if __name__ == '__main__':
    main()
