import math
def main():
    x1, y1, x2, y2 = map(float, input().split())
    b = abs(x2 - x1)
    h = abs(y2 - y1)
    d = math.sqrt(b ** 2 + h ** 2)
    print("{0:.8f}".format(d))


if __name__ == "__main__":
    main()